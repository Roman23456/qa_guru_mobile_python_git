import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class SearchScreen:
    @allure.step("Открыть строку поиска")
    def open(self):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        return self

    @allure.step("Ввести поисковый запрос '{query}'")
    def search(self, query: str):
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")
        ).type(query)
        return self

    @allure.step("Убедиться, что список результатов не пустой")
    def should_have_results(self):
        browser.all(
            (
                AppiumBy.XPATH,
                "//androidx.compose.ui.platform.ComposeView"
                '//android.view.View[@clickable="true"]',
            )
        ).should(have.size_greater_than(0))
        return self

    @allure.step("Убедиться, что первый результат содержит '{text}'")
    def first_result_should_have_text(self, text: str):
        browser.all(
            (
                AppiumBy.XPATH,
                "//androidx.compose.ui.platform.ComposeView"
                '//android.widget.TextView[@index="0"]',
            )
        ).first.should(have.text(text))
        return self

    @allure.step("Открыть первый результат")
    def open_first_result(self):
        browser.all(
            (
                AppiumBy.XPATH,
                "//androidx.compose.ui.platform.ComposeView"
                '//android.view.View[@clickable="true"]',
            )
        ).first.click()
        return self


search_screen = SearchScreen()
