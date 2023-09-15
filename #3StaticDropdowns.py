import time

from select import select

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

optionsobj = webdriver.ChromeOptions()
optionsobj.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=optionsobj)

#serviceobject = Service("C:\Pinky\PythonSelenium\drivers\chromedriver.exe")
#driver = webdriver.Chrome(service=serviceobject)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/#")

#  Handling static dropdown: currency field

currency = Select(driver.find_element(By.CSS_SELECTOR,"#ctl00_mainContent_DropDownListCurrency"))
currency.select_by_index(0)
time.sleep(3)
currency.select_by_visible_text("AED")
time.sleep(2)
currency.select_by_value("USD")

#  Handling static dropdown: passenger field

#staticobject = Select(driver.find_element(By.XPATH,"//div[@class='row1 adult-infant-child']//descendant::p"))  # Select only works on <select> elements, not on p
print(driver.find_element(By.CSS_SELECTOR,"#divpaxinfo").text)
driver.find_element(By.CSS_SELECTOR,"#divpaxinfo").click()
time.sleep(2)

for i in range(2):
    driver.find_element(By.XPATH,
                        "//div[@class='row1 adult-infant-child']/div[3]/div[@id='divAdult']/div[2]/span[@id='hrefIncAdt']").click()
    print(driver.find_element(By.CSS_SELECTOR,"#divpaxinfo").text)
    break
driver.find_element(By.XPATH,"//div[@class='row1 adult-infant-child']/div[3]/div[@id='divChild']/div[2]/span[@id='hrefIncChd']").click()
print(driver.find_element(By.CSS_SELECTOR,"#divpaxinfo").text)


driver.close()



