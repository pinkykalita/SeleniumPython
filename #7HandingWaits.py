import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

#serviceobject = Service("C:\Pinky\PythonSelenium\drivers\chromedriver.exe")
#driver = webdriver.Chrome(service=serviceobject)

chromeobject = webdriver.ChromeOptions()
chromeobject.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chromeobject)

driver.maximize_window()
driver.get ("https://rahulshettyacademy.com/seleniumPractise/#/")

# use of implicit waits
driver.implicitly_wait(5) # now each line will wait for at least 5 sec to find the web element; applicable at Global level

# search the vegetable
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("berr")
driver.find_element(By.CSS_SELECTOR," .search-button").click()
time.sleep(2)

# Get number of vegetables returned
# veges = driver.find_elements(By.CSS_SELECTOR,".product")
veges = driver.find_elements(By.XPATH,"//*/div[@class= 'product']")
print(len(veges))

# for i in veges:
#     i.find_element(By.CSS_SELECTOR,"div:nth-child(5)[class$='product-action'] [type='button']").click()  # this is called chaining. driver will lo

# Add all the vegetables to the cart
for vegetable in veges:
    vegetable.find_element(By.XPATH,"//*/div[@class= 'product']/div[.='ADD TO CART']").click()

# Go to checkout screen
driver.find_element(By.CSS_SELECTOR,"img[alt*='Cart']").click()
vegetable.find_element(By.XPATH,"//button[. = 'PROCEED TO CHECKOUT']").click()
# vegetable.find_element(By.XPATH,"//button[text() = 'PROCEED TO CHECKOUT']").click()

# assert number of items in cart same as items actually added to cart
itemsincart = driver.find_elements(By.XPATH,"//tbody/tr")
print(len(itemsincart))
assert len(veges) == len(itemsincart)


# to count the total amount of the cart
columns = driver.find_elements(By.XPATH, "//tr/td[5]")
#for column in columns:

# to apply promo code
driver.find_element(By.CSS_SELECTOR,".promoWrapper input[placeholder='Enter promo code']").send_keys("rahulshettyacademy")
# driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
#time.sleep(15)
# to explicitly wait for a step longer use explicit wait
wait = WebDriverWait(driver, 15)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".promoInfo")))
promotext = driver.find_element(By.CSS_SELECTOR,".promoInfo").text
assert "Code applied ..!" in promotext
print(promotext)

driver.close()