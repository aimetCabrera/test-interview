from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="./driver/chromedriver.exe")
driver.get("https://www.saucedemo.com/")
time.sleep(2)
userName =driver.find_element(By.ID, "user-name")
userName.send_keys("standard_user")
userPassword= driver.find_element(By.ID, "password")
userPassword.send_keys("secret_sauce")
time.sleep(2)
btnLogin= driver.find_element(By.ID, "login-button")
btnLogin.click()
time.sleep(2)
seleccionarArticulo1= driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack")
seleccionarArticulo1.click()
seleccionarArticulo2= driver.find_element(By.NAME, "add-to-cart-sauce-labs-bike-light")
seleccionarArticulo2.click()
compra =driver.find_element(By.CLASS_NAME, "shopping_cart_link")
compra.click()
chequearCompra= driver.find_element(By.ID, "checkout")
chequearCompra.click()
name =driver.find_element(By.ID, "first-name")
name.send_keys("Lucia")
name2 =driver.find_element(By.ID, "last-name")
name2.send_keys("Perez")
cpostal =driver.find_element(By.ID, "postal-code")
cpostal.send_keys("10500")
continuar =driver.find_element(By.ID, "continue")
continuar.click()
time.sleep(2)
fin =driver.find_element(By.ID, "finish")
fin.click()

driver.close()