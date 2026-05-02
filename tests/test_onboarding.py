import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import be, browser


@allure.feature('Onboarding')
@allure.story('Пользователь может пропустить онбординг')
def test_skip_onboarding():
    with allure.step('Нажать кнопку "Пропустить" на экране онбординга'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()

    with allure.step('Убедиться, что отображается главный экран с поиском'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_container')).should(be.visible)
