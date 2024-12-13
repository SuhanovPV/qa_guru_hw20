import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_welcome_screen():
    with allure.step('Check open welckome screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')). \
            should(have.text('The Free Encyclopedia\n…in over 300 languages'))

    with allure.step('Go to second page of welcome screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')). \
            should(have.text('New ways to explore'))

    with allure.step('Go to third page of welcome screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')). \
            should(have.text('Reading lists with sync'))

    with allure.step('Go to fourth page of welcome screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')). \
            should(have.text('Data & Privacy'))

    with allure.step('Close welcome screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button')).click()
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.TextView')).first.should(have.text('Search Wikipedia'))
