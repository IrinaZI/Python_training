import pytest
from fixture.application import Application

fixture = None

@pytest.fixture
def app(request):
    global fixture
    baseUrl = request.config.getoption("--baseUrl")
    browser = request.config.getoption("--browser")
    if fixture is None:
        fixture = Application(browser=browser, base_url=baseUrl)
    else:
       if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=baseUrl)
    fixture.session.ensure_Login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_Logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")