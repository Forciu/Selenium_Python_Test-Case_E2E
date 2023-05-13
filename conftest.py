import pytest
from selenium import webdriver
import time
driver = None


def pytest_addoption(parser):  # Terminal options for another browser
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")  # Performs fixture for entire class not for each test separately
def setup(request):  # Main settings for all test cases
    global driver
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":  #Chrome invocation
        driver = webdriver.Chrome(executable_path="DriverEXE/chromedriver.exe")
    elif browser_name == "firefox":  # Firefox's invocation Gecko Driver
        driver = webdriver.Firefox(executable_path="DriverEXE/geckodriver.exe")

    driver.get("https://rahulshettyacademy.com/angularpractice")
    driver.maximize_window()
    driver.implicitly_wait(6)  # Global timeout
    request.cls.driver = driver  # Send driver to class object test_e2e
    yield
    time.sleep(5)
    print('Test Pass')
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """PyTest plugin to capture errors with screenshot"""
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
