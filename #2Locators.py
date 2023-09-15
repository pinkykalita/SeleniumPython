from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# ChromeOptions is a concept in Selenium WebDriver for manipulating various properties of the Chrome driver
# my test was getting automatically closed on using "Service", so i am using this ChromeOption
options = webdriver.ChromeOptions()  # Create an object for ChromeOptions
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

#serviceobject = Service("C:\Pinky\PythonSelenium\drivers\chromedriver.exe")
#driver = webdriver.Chrome(service=serviceobject)

## practicing basic findelements locators
def practiceBasics():  # putting all the code in a function for clarity
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    driver.find_element(By.LINK_TEXT,"Home").click()  # Use this when you know the link text(href) used within an anchor tag
    driver.find_element(By.PARTIAL_LINK_TEXT, "Sho")  # using partial text of the link label
    driver.back()
    driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Pinky Kalita")  ## This will return 2 elements
    driver.find_element(By.CSS_SELECTOR, "input[name='name']").clear()  ## clears the text field
    driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys(Keys.CONTROL + "a" + Keys.CLEAR)  ## this will clear both the fields
    driver.find_element(By.CSS_SELECTOR, "div[class='form-group'] input[name='name']").send_keys("New Name")  ## Css selector
    driver.find_element(By.NAME,"email").send_keys("pinky@gmail.com")  # Use this when you know the name attribute of an element
    driver.find_element(By.ID,"exampleInputPassword1").send_keys("test")  # when you know the id attribute of an element
    driver.find_element(By.CLASS_NAME, "ng-pristine").send_keys(" Hello Again!")  # dont use the whole calss name (form-control ng-pristine ng-invalid ng-touched) as it has space inbetween, instead use only 1 class name inside
    driver.find_element(By.ID, "exampleCheck1").click()
    driver.find_element(By.XPATH,"//*[@id='exampleCheck1']").click()
    driver.find_element(By.CSS_SELECTOR,"input[id='exampleCheck1']").click() ## using Css Selector
    driver.find_element(By.ID, "exampleInputPassword1").send_keys(Keys.ENTER)  # send_keys(Keys. ) to send a specific key from keyboard
    #on pressing Enter, form submitted message should be displayed->Enter will submit the form
    successmessage = driver.find_element(By.CLASS_NAME,"alert-success").text  # text text will grab the text from webelement
    print(successmessage)  ## "Success! The Form has been submitted successfully!."
    assert "Success!" in successmessage


## practicing Xpath with different types
def practiceXpath():
    driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
    driver.maximize_window()
    driver.find_element(By.XPATH,"//td//input[@value='RoundTrip']").click()  ## //tagname[@attribute=value]
    driver.find_element(By.XPATH,"//div[contains(@id,'familyandfriend')]").click()  ## //tagname[contains(@attribute,value]
    driver.find_element(By.XPATH,"//label[starts-with(text(),' Indian Armed Forces')]").click()  ## //tagname[starts-with(@attribute,value]




practiceBasics()  # calling the function
#practiceXpath()
