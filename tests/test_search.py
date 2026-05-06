import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@allure.feature("Search")
@allure.story("Пользователь может найти статью через поиск")
def test_search_returns_results():
    with allure.step("Пропустить онбординг"):
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id"
                          "/fragment_onboarding_skip_button")
        ).click()

    with allure.step("Открыть строку поиска"):
        browser.element((AppiumBy.ACCESSIBILITY_ID,
                        "Search Wikipedia")).click()

    with allure.step('Ввести поисковый запрос "Python"'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id"
                                      "/search_src_text")).type(
            "Python"
        )

    with allure.step("Убедиться, что список результатов не пустой"):
        browser.all(
            (
                AppiumBy.XPATH,
                "//androidx.compose.ui.platform.ComposeView"
                '//android.view.View[@clickable="true"]',
            )
        ).should(have.size_greater_than(0))


@allure.feature("Search")
@allure.story("Первый результат поиска содержит поисковый запрос в заголовке")
def test_search_result_title_matches_query():
    with allure.step("Пропустить онбординг"):
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id"
                          "/fragment_onboarding_skip_button")
        ).click()

    with allure.step("Открыть строку поиска"):
        browser.element((AppiumBy.ACCESSIBILITY_ID,
                        "Search Wikipedia")).click()

    with allure.step('Ввести поисковый запрос "Appium"'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id"
                                      "/search_src_text")).type(
            "Appium"
        )
    with allure.step('Убедиться, что первый '
                     'результат содержит слово "Appium"'):
        browser.all(
            (
                AppiumBy.XPATH,
                "//androidx.compose.ui.platform.ComposeView"
                '//android.widget.TextView[@index="0"]',
            )
        ).first.should(have.text("Appium"))
