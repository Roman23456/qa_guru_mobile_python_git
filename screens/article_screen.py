import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import be, browser, have


class ArticleScreen:
    @allure.step('Закрыть попап "Wikipedia games", если он появился')
    def close_popup_if_visible(self):
        close_button = browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/closeButton")
        )
        if close_button.with_(timeout=3).wait.until(be.visible):
            close_button.click()
        return self

    @allure.step("Убедиться, что заголовок статьи содержит '{text}'")
    def should_have_title(self, text: str):
        browser.element(
            (
                AppiumBy.XPATH,
                f'//*[@resource-id="org.wikipedia.alpha:id/view_page_title_text"]'
                f' | //android.view.View[@content-desc="{text}"]'
                f' | //android.widget.TextView[contains(@text,"{text}")]',
            )
        ).should(have.text(text))
        return self


article_screen = ArticleScreen()
