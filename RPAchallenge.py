from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()

# Abre uma página de exemplo
driver.get("https://rpachallenge.com/")

time.sleep(1)

spreadsheet_data = pd.read_excel("challenge.xlsx", sheet_name="Sheet1")

start = driver.find_element(By.CLASS_NAME, "waves-effect.col.s12.m12.l12.btn-large.uiColorButton")
start.click()
for index, row in spreadsheet_data.iterrows():
    Address = driver.find_element(By.XPATH, "//input[contains(@ng-reflect-name, 'labelAddress')]").send_keys(row['Address'])

    first_name = driver.find_element(By.XPATH, "//input[contains(@ng-reflect-name, 'labelFirstName')]").send_keys(row['First Name'])

    last_name = driver.find_element(By.XPATH, "//input[contains(@ng-reflect-name, 'labelLastName')]").send_keys(row['Last Name '])

    company_name = driver.find_element(By.XPATH, "//input[contains(@ng-reflect-name, 'labelCompanyName')]").send_keys(row['Company Name'])

    phone_number = driver.find_element(By.XPATH, "//input[contains(@ng-reflect-name, 'labelPhone')]").send_keys(row['Phone Number'])

    email = driver.find_element(By.XPATH, "//input[contains(@ng-reflect-name, 'labelEmail')]").send_keys(row['Email'])

    role_in_company = driver.find_element(By.XPATH, "//input[contains(@ng-reflect-name, 'labelRole')]").send_keys(row['Role in Company'])

    submit = driver.find_element(By.CLASS_NAME, "btn.uiColorButton").click()


x = input("")
driver.quit()
