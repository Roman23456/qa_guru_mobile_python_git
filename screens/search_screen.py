import allure
from selene import browser, have


class SearchScreen:
    @allure.step("Открыть строку поиска")
    def open(self):
        browser.element('Search Wikipedia').click()
        return self

    @allure.step("Ввести поисковый запрос '{query}'")
    def search(self, query: str):
        browser.element('#search_src_text').type(query)
        return self

    @allure.step("Убедиться, что список результатов не пустой")
    def should_have_results(self):
        browser.all('#page_list_item_container').should(have.size_greater_than(0))
        return self

    @allure.step("Убедиться, что первый результат содержит '{text}'")
    def first_result_should_have_text(self, text: str):
        browser.all('#page_list_item_title').first.should(have.text(text))
        return self

    @allure.step("Открыть первый результат")
    def open_first_result(self):
        browser.all('#page_list_item_container').first.click()
        return self


search_screen = SearchScreen()
