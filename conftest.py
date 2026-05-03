import base64

import allure
import pytest
import requests
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selene import browser

from config import BrowserStackConfig, config, context


def _local_options() -> UiAutomator2Options:
    options = UiAutomator2Options()
    options.set_capability('appium:app', config.app)
    options.set_capability('appium:deviceName', config.device_name)
    options.set_capability('appium:platformVersion', config.platform_version)
    options.set_capability('appium:newCommandTimeout', 3600)
    options.set_capability('appium:fullReset', False)
    return options


def _browserstack_options() -> UiAutomator2Options:
    options = UiAutomator2Options()
    options.set_capability('bstack:options', {
        'userName': config.user_name,
        'accessKey': config.access_key,
        'projectName': config.project,
        'buildName': config.build,
        'sessionName': config.name,
        'deviceName': config.device,
        'osVersion': config.os_version,
    })
    options.set_capability('appium:app', config.app)
    options.set_capability('appium:autoGrantPermissions', True)
    return options


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    if context == 'local':
        driver = webdriver.Remote(config.appium_url, options=_local_options())
    else:
        driver = webdriver.Remote(
            'https://hub.browserstack.com/wd/hub',
            options=_browserstack_options(),
        )

    browser.config.driver = driver
    browser.config.timeout = 10.0

    if context == 'local':
        try:
            browser.driver.start_recording_screen()
        except Exception:
            pass

    yield

    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='Screenshot',
        attachment_type=allure.attachment_type.PNG,
    )

    if context == 'local':
        try:
            video_b64 = browser.driver.stop_recording_screen()
            if video_b64:
                allure.attach(
                    base64.b64decode(video_b64),
                    name='Video',
                    attachment_type=allure.attachment_type.MP4,
                )
        except Exception:
            pass

    if context == 'browserstack':
        _attach_browserstack_session(config)

    browser.quit()


def _attach_browserstack_session(cfg: BrowserStackConfig) -> None:
    session_id = browser.driver.session_id
    try:
        response = requests.get(
            f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
            auth=(cfg.user_name, cfg.access_key),
            timeout=10,
        )
        data = response.json().get('automation_session', {})
        if url := data.get('browser_url'):
            allure.attach(
                f'<html><head><meta http-equiv="refresh" content="0;url={url}"></head>'
                f'<body><a href="{url}">Open BrowserStack Session</a></body></html>',
                name='BrowserStack Session',
                attachment_type=allure.attachment_type.HTML,
            )
        if video_url := data.get('video_url'):
            allure.attach(
                f'<html><body><video width="100%" controls><source src="{video_url}" type="video/mp4"></video></body></html>',
                name='Video',
                attachment_type=allure.attachment_type.HTML,
            )
    except Exception:
        pass
