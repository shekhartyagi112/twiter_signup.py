from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://twitter.com/")
driver.find_element(By.XPATH,"//span[contains(text(),'Create account')]").click()
time.sleep(2)
driver.find_element(By.NAME,"name").send_keys("vijay kumar bharti")
time.sleep(2)
driver.find_element(By.NAME,"phone_number").send_keys("9639980052")
time.sleep(2)
driver.find_element(By.XPATH,"//option[normalize-space()='January']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//option[@value='28']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//option[@value='1998']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//span[contains(text(),'Next')]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//span[contains(text(),'Next')]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//span[@class='css-901oao css-16my406 css-1hf3ou5 r-poiln3 r-1inkyih r-rjixqe r-bcqeeo r-qvutc0']//span[@class='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'][normalize-space()='Sign up']").click()

time.sleep(10)
driver.close()
