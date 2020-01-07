
from pytest import fixture
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome OR firefox")


@fixture(params=["chrome","firefox"], scope="class")
def test_setup(request):
    global driver
    if request.param == "chrome":
        # Local webdriver implementation
        # web_driver = webdriver.Chrome()
        # Remote WebDriver implementation
        driver = webdriver.Remote(
            command_executor='http://192.168.29.191:4545/wd/hub',
            desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
    if request.param == "firefox":
        # Local webdriver implementation
        # web_driver = webdriver.Firefox()
        # Remote WebDriver implementation
        driver = webdriver.Remote(
            command_executor='http://192.168.29.191:4545/wd/hub',
            desired_capabilities={'browserName': 'firefox'})
    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield
    driver.close()
    print("Test completed")
