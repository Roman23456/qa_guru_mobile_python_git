import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@allure.feature('Articles')
@allure.story('Пользователь может открыть статью из результатов поиска')
def test_open_article_from_search():
    with allure.step('Пропустить онбординг'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()

    with allure.step('Открыть строку поиска'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()

    with allure.step('Ввести поисковый запрос "Appium"'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Appium')

    with allure.step('Открыть первый результат'):
        browser.all((AppiumBy.XPATH, '//androidx.compose.ui.platform.ComposeView'
                                     '//android.view.View[@clickable="true"]')).first.click()

    with allure.step('Закрыть попап "Wikipedia games", если он появился'):
        try:
            browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/closeButton')).with_(timeout=3).click()
        except Exception:
            pass

    with (allure.step('Убедиться, что заголовок статьи содержит "Appium"')):
        browser.element((AppiumBy.XPATH, '//*[@resource-id="org.wikipedia.alpha:id'
                                         '/view_page_title_text"]'
                                         ' | //android.view.View[@content-desc="Appium"]'
                                         ' | //android.widget.TextView[contains(@text,"Appium")]')).should(
            have.text('Appium')
        )
