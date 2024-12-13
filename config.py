import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from pydantic_settings import BaseSettings
from selene import browser
from qa_guru_hw20.utils import path_helper

class Config(BaseSettings):
    deviceName: str = ''
    app: str = ''
    appWaitActivity: str = ''
    appActivity: str = ''
    remote_url: str = ''
    timeout: float = 8.0
    platformVersion: str = ''
    sessionName: str = ''
    projectName: str = ''
    name: str = ''
    accessKey: str = ''


def load_config_from_env(context):
    if context in ['local', 'remote', 'emulator']:
        config = Config(_env_file=path_helper.abs_path_from_project(f'.env.{context}'))
    else:
        raise KeyError
    return config


def set_options(config, context):
    options = UiAutomator2Options().load_capabilities(
        {
            'deviceName': config.deviceName,
            'appWaitActivity': config.appWaitActivity,
            'appActivity': config.appActivity,
        }
    )

    options.set_capability('app', (
        config.app if context == 'remote' else path_helper.abs_path_from_project(config.app))
    )
    if context == 'remote':
        options.set_capability('platformVersion', config.platformVersion)
        options.set_capability('bstack:options', {
            "sessionName": config.sessionName,
            "projectName": config.projectName,
            "userName": config.name,
            "accessKey": config.accessKey
        })
    return options


def set_browser(context):
    config = load_config_from_env(context)
    options = set_options(config, context)
    browser.config.timeout = config.timeout
    browser.config.driver = webdriver.Remote(config.remote_url, options=options)
