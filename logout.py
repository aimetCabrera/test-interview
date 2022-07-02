import self as self
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="./driver/chromedriver.exe")
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(2)

userName = driver.find_element(By.ID, "user-name")
userName.send_keys("standard_user")
userPassword = driver.find_element(By.ID, "password")
userPassword.send_keys("secret_sauce")
time.sleep(2)
btnLogin = driver.find_element(By.ID, "login-button")
btnLogin.click()
time.sleep(2)
btn1 = driver.find_element(By.ID, "react-burger-menu-btn")
btn1.click()
#btn2 =driver.find_element(By.ID, "logout_sidebar_link")
btn2 = driver.find_element(By.CLASS_NAME, "bm-menu")
btn2.click()

driver.close()
