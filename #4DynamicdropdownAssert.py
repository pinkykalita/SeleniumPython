import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chromeobject = webdriver.ChromeOptions()
chromeobject.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chromeobject)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/#")

driver.find_element(By.CSS_SELECTOR,"#autosuggest").send_keys("in")  # type user input to get the dropdown
time.sleep(2)
countrysuggestions = driver.find_elements(By.CSS_SELECTOR,"#ui-id-1 li a")  # get all the content in the drop down
print(len(countrysuggestions))  # printing the number of suggestions in the dropdown

# Next we have to go through each country till we find India in the country list
for country in countrysuggestions:
    if country.text == "India":
        country.click()
        break

# Select From City
driver.find_element(By.CSS_SELECTOR, "#ctl00_mainContent_ddl_originStation1_CTXT").send_keys("h")
time.sleep(2)
fromcity = driver.find_elements(By.XPATH, "//div[@class='dropdownDiv']/ul/li/a")
print(len(fromcity))
for fromc in fromcity:
    if fromc.text == "Hyderabad (HYD)":
        fromc.click()
        break

# Select To City
driver.find_element(By.CSS_SELECTOR, "#ctl00_mainContent_ddl_destinationStation1_CTXT").send_keys("g")
time.sleep(2)
tocity = driver.find_elements(By.CSS_SELECTOR,"#dropdownGroup1 .dropdownDiv ul li a")
print(len(tocity))
for toc in tocity:
    if toc.text == "Guwahati (GAU)":
        toc.click()
        break

# print(driver.find_element(By.CSS_SELECTOR, "#ctl00_mainContent_ddl_destinationStation1_CTXT").text)
# this will not print the city name in console
# as the text was dynamically edited by the automation code so the text cannot be captured using text command
# use get_attibute("value") cmd to catch the dynamic values from the webelement

print("Arrival: "+ driver.find_element(By.CSS_SELECTOR, "#ctl00_mainContent_ddl_originStation1_CTXT").get_attribute("value"))
print("Destination: " + driver.find_element(By.CSS_SELECTOR, "#ctl00_mainContent_ddl_destinationStation1_CTXT").get_attribute("value"))

# Assert dynamic values
assert (driver.find_element(By.CSS_SELECTOR,"#autosuggest").get_attribute("value")) == "India"

#driver.close()
