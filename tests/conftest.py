import pytest
from selenium import webdriver
driver_local = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver_local
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver_local = webdriver.Chrome()
    elif browser_name == "firefox":
        driver_local = webdriver.Firefox()
    elif browser_name == "safari":
        driver_local = webdriver.Safari()
    elif browser_name == "IE":
        print("IE driver")
    driver_local.get("https://rahulshettyacademy.com/angularpractice/")
    driver_local.maximize_window()
    driver_local.implicitly_wait(5)

    request.cls.driver = driver_local
    yield
    driver_local.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
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
    driver_local.get_screenshot_as_file(name)

