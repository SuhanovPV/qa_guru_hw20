import allure_commons
import config
import pytest
from selene import support, browser


def pytest_addoption(parser):
    parser.addoption(
        '--context',
        default='emulator',
        help='--context: local, emulator or remote'
    )


@pytest.fixture(scope='function', autouse=True)
def mobile_settings(request):
    context = request.config.getoption('--context')
    config.set_browser(context)

    yield

    browser.quit()
