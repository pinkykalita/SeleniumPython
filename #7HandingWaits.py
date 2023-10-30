from select import select
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select


#serviceobject = Service("C:\Pinky\PythonSelenium\drivers\chromedriver.exe")
#driver = webdriver.Chrome(service=serviceobject)

chromeobject = webdriver.ChromeOptions()
chromeobject.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chromeobject)

driver.maximize_window()
driver.get ("https://rahulshettyacademy.com/seleniumPractise/#/")

# use of implicit waits
driver.implicitly_wait(10) # now each line will wait for at least 5 sec to find the web element; applicable at Global level

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

# Add all the vegetables to the cart also Assert all search result displayed are same as the list
ExpectedList = ["Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
ActualList = [] # create empty list
for vegetable in veges:
    ActualList.append(vegetable.find_element(By.XPATH,"//*/div[@class= 'product']/h4[@class='product-name']").text)
    vegetable.find_element(By.XPATH,"//*/div[@class= 'product']/div[.='ADD TO CART']").click()
#assert ActualList == ExpectedList
print(ActualList)

# Go to checkout screen
driver.find_element(By.CSS_SELECTOR,"img[alt*='Cart']").click()
vegetable.find_element(By.XPATH,"//button[. = 'PROCEED TO CHECKOUT']").click()
# vegetable.find_element(By.XPATH,"//button[text() = 'PROCEED TO CHECKOUT']").click()

# assert number of items in cart same as items actually added to cart
itemsincart = driver.find_elements(By.XPATH,"//tbody/tr")
print(len(itemsincart))
assert len(veges) == len(itemsincart)

# explicit wait
# to explicitly wait for a step longer use explicit wait
wait = WebDriverWait(driver, 15)  # explicit wait to specifically wait before a step for a certain time so that the webelement gets visible


# to count the total amount of the cart
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"td:nth-child(5)")))
columns = driver.find_elements(By.CSS_SELECTOR, "td:nth-child(5) p")
sum = 0
for price in columns: # price will contain 1 column value at a time
    sum = sum + int(price.text) # reading each price and converting amount text to int for sum
print("Sum of products cost is: " + str(sum))

# assert sum is same as the total cart amount
carttotal = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text) # to convert the total amount to int for assertion
assert sum == carttotal
print("cart total is: " + str(carttotal))


# to apply promo code
driver.find_element(By.CSS_SELECTOR,".promoWrapper input[placeholder='Enter promo code']").send_keys("rahulshettyacademy")
# driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".promoInfo")))
promotext = driver.find_element(By.CSS_SELECTOR,".promoInfo").text
assert "Code applied ..!" in promotext
print(promotext)

# Assert that discounted amount is always less than the Total amount after applying discount 
discountedTotal = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
print("Payable amount after discount: " + str(discountedTotal))
assert carttotal > discountedTotal

# Place order
driver.find_element(By.XPATH, "//*/button[text() = 'Place Order']").click()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//select[1]")))
country = Select(driver.find_element(By.XPATH,"//select"))  # static dropdown: country
country.select_by_value("India")
driver.find_element(By.CSS_SELECTOR,".chkAgree").click()
#wait.until(expected_conditions.visibility_of_element_located(By.XPATH,"//span[contains(text(),'Proceed')]"))
#driver.find_element(By.XPATH,"//button[text()='Proceed']").click()
driver.find_element(By.CSS_SELECTOR,"div[class='wrapperTwo'] button").click()
#driver.find_element(By.XPATH,"//span[contains(text(),'Proceed')]").click()
# assert suucessful order placed message 

driver.close()