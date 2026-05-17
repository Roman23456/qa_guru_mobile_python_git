import allure

from screens.onboarding_screen import onboarding_screen
from screens.search_screen import search_screen


@allure.feature("Search")
@allure.story("Пользователь может найти статью через поиск")
def test_search_returns_results():
    onboarding_screen.skip()
    search_screen.open().search("Python").should_have_results()


@allure.feature("Search")
@allure.story("Первый результат поиска содержит поисковый запрос в заголовке")
def test_search_result_title_matches_query():
    onboarding_screen.skip()
    search_screen.open().search("Appium").first_result_should_have_text("Appium")
