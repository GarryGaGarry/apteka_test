import time
import warnings

import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.opera.options import Options as OperaOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver import Chrome, ChromeOptions
import pytest
from selene import Config, Browser
from selenium import webdriver

from configuration import Configuration


def pytest_addoption(parser):
    parser.addoption('--url',
                     type=str,
                     help='Base url to the tested object')
    parser.addoption('--headless',
                     help='Headless options: "true" or "false"',
                     type=bool,
                     choices=(True, False))
    parser.addoption('--browser-type',
                     type=str,
                     help='Option to define web or mobile browser',
                     choices=('web', 'mobile'))
    parser.addoption('--mobile-device',
                     type=str,
                     help='Option to define mobile device. See the allowed devices in the configuration.py')
    parser.addoption('--browser-size',
                     type=str,
                     help='The size of the browser window. Example value 1280,1024')


def check_configuration():
    if Configuration.browser_type == 'web' and Configuration.mobile_device:
        Configuration.mobile_device = None
        warnings.warn(UserWarning("Browser type is web, mobile device parameter is ignored"))

    if Configuration.browser_type == 'mobile':
        if Configuration.browser_size:
            Configuration.browser_size = None
            warning = "Browser type is mobile, so browser size will be ignored"
            warnings.warn(UserWarning(warning))

        if Configuration.mobile_device is None:
            Configuration.mobile_device = Configuration.supported_devices[0]
            warning = f"Browser type is mobile, but mobile device is not selected," \
                      f" so default device({Configuration.mobile_device}) is selected"
            warnings.warn(UserWarning(warning))

        if Configuration.mobile_device not in Configuration.supported_devices:
            raise ValueError(f"Device({Configuration.mobile_device}) not found in the list of supported devices")


@pytest.fixture(autouse=True, scope='session')
def config(request):
    Configuration.base_url = request.config.getoption("--url") or Configuration.base_url
    Configuration.headless = request.config.getoption("--headless") or Configuration.headless
    Configuration.browser_type = request.config.getoption("--browser-type") or Configuration.browser_type
    Configuration.browser_size = request.config.getoption("--browser-size") or Configuration.browser_size
    Configuration.mobile_device = request.config.getoption("--mobile-device") or Configuration.mobile_device
    check_configuration()
    return Configuration


@pytest.fixture(autouse=True, scope='session')
def browser(config):
    options = ChromeOptions()
    if Configuration.browser_type == 'mobile':
        mobile_emulation = {"deviceName": Configuration.mobile_device}
        options.add_experimental_option("mobileEmulation", mobile_emulation)
    if Configuration.browser_size:
        options.add_argument(f"--window-size={Configuration.browser_size}")
    if Configuration.headless:
        options.headless = True

    if Configuration.remote_driver_url:
        driver = webdriver.Remote(
            command_executor=Configuration.remote_driver_url,
            desired_capabilities=Configuration.selenoid_capabilities,
            options=options,
        )
    else:
        driver = Chrome(chrome_options=options)

    browser = Browser(Config(
        driver=driver,
        timeout=Configuration.timeout))

    yield browser

    browser.quit()


@pytest.fixture(autouse=True, scope='session')
def session_end_time():
    yield
    now = time.time()
    print('--')
    print('finished : {}'.format(time.strftime('%d %b %X', time.localtime(now))))
    print('-----------------')


@pytest.fixture(autouse=True)
def test_time():
    start = time.time()
    yield
    stop = time.time()
    delta = stop - start
    print('\ntest duration : {:0.3} seconds'.format(delta))
