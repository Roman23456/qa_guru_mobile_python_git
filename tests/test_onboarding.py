import allure

from screens.onboarding_screen import onboarding_screen


@allure.feature("Onboarding")
@allure.story("Пользователь может пропустить онбординг")
def test_skip_onboarding():
    onboarding_screen.skip()
    onboarding_screen.should_be_visible()
