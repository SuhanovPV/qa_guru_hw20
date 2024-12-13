import allure
import allure_commons
import config
import pytest
from selene import support, browser

from qa_guru_hw20 import allure_attach


def pytest_addoption(parser):
    parser.addoption(
        '--context',
        default='remote',
        help='--context: local, emulator or remote'
    )


@pytest.fixture(scope='function', autouse=True)
def mobile_settings(request):
    context = request.config.getoption('--context')
    config.set_browser(context)

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    allure_attach.bstack_screenshot(browser)

    allure_attach.bstack_page_source(browser)

    session_id = browser.driver.session_id

    with allure.step(f'tear down app session id {session_id}'):
        browser.quit()

    if context == 'remote':
        allure_attach.video(session_id)
