import allure
import requests
import config


def bstack_page_source(browser):
    allure.attach(
        body=browser.driver.page_source,
        name='screen_xml_dump',
        attachment_type=allure.attachment_type.XML
    )


def bstack_screenshot(browser):
    allure.attach(
        body=browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG
    )


def video(session_id):
    conf = config.load_config_from_env('remote')
    bstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(conf.name, conf.accessKey)
    ).json()
    video_url = bstack_session['automation_session']['video_url']
    allure.attach(
        '<html><body><video width="100%" height="100%" controls autoplay>'
        f'<source src={video_url} type="video/mp4">'
        '</video></body></html>',
        name='video_rec',
        attachment_type=allure.attachment_type.HTML
    )
