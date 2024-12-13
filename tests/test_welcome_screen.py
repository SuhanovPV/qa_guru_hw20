import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_welcome_screen():
    browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')). \
        should(have.text('The Free Encyclopedia\n…in over 300 languages'))
    browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
    browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')). \
        should(have.text('New ways to explore'))
    browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
    browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')). \
        should(have.text('Reading lists with sync'))
    browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
    browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')). \
        should(have.text('Data & Privacy'))
    browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button')).click()
    browser.all((AppiumBy.CLASS_NAME, 'android.widget.TextView')).first.should(have.text('Search Wikipedia'))

