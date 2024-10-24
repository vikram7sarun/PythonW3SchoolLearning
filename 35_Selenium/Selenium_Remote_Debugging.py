# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# chrome_options = Options()
# Options.add_argument('--remote-debugging-port=9226')
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://acme-test.uipath.com/")


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
# chrome_options.add_experimental_option("debuggerAddress", "http://localhost:9214")
chrome_options.add_argument('--remote-debugging-port=9214')
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://acme-test.uipath.com/")
driver.find_element(By.ID,'email').send_keys("vikic3110@gmail.com")
driver.find_element(By.ID,'password').send_keys("Test@123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
print("...............")


