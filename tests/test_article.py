import allure

from screens.article_screen import article_screen
from screens.onboarding_screen import onboarding_screen
from screens.search_screen import search_screen


@allure.feature("Articles")
@allure.story("Пользователь может открыть статью из результатов поиска")
def test_open_article_from_search():
    onboarding_screen.skip()
    search_screen.open().search("Appium").open_first_result()
    article_screen.close_popup_if_visible()
    article_screen.should_have_title("Appium")
