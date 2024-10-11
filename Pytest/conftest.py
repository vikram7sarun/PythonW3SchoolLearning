import pytest


@pytest.fixture(scope="function",autouse=True)
def SetUp():
    print("Launch Browser")
    print("Login")
    print("Browse Products")
    yield
    print("Logout form the application")
    print("Close browser")