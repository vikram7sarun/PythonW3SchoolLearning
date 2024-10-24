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
lpt = driver.title
print(lpt)
driver.find_element(By.XPATH, "//input[@title='Search']").send_keys("Python")
menu = driver.find_element(By.CSS_SELECTOR,".nav")
hidden_submenu = driver.find_element(By.CSS_SELECTOR,".nav # submenu1")
actions = ActionChains(driver)
actions.move_to_element(menu)
actions.click(hidden_submenu)
actions.perform()

