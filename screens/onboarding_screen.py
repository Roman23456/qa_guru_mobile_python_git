import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import be, browser


class OnboardingScreen:
    @allure.step('Нажать кнопку "Пропустить" на экране онбординга')
    def skip(self):
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")
        ).click()
        return self

    @allure.step("Убедиться, что отображается главный экран с поиском")
    def should_be_visible(self):
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/search_container")
        ).should(be.visible)
        return self


onboarding_screen = OnboardingScreen()
