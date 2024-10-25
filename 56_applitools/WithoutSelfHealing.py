from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://acme-test.uipath.com/login")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("test31@gmail.com")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Testing@123")
driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
lpt = driver.title

if lpt == "ACME System 1 - Dashboard":
    assert True
    print("ACME Login Success")
else:
    assert False
    print("ACME Login in UnSuccessfull")


