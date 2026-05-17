import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import be, browser


class OnboardingScreen:
    @allure.step('Нажать кнопку "Пропустить" на экране онбординга')
    def skip(self):
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")
        ).click()
        close_btn = browser.element((AppiumBy.ACCESSIBILITY_ID, "Close"))
        if close_btn.with_(timeout=3).wait.until(be.visible):
            close_btn.click()
        return self

    @allure.step("Убедиться, что отображается главный экран с поиском")
    def should_be_visible(self):
        browser.element(
            (AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")
        ).should(be.visible)
        return self


onboarding_screen = OnboardingScreen()
