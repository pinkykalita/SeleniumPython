from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serviceobject = Service("C:\Pinky\PythonSelenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=serviceobject)  # Open browser.
driver.maximize_window()  # Maximize the browser window.
driver.get("http://qatechhub.com")  # Navigate to “http://qatechhub.com”.
print(driver.title)  # Print the title of the Page
print(driver.current_url)  # Print the current URL
driver.get("https://www.facebook.com")  # Navigate to the Facebook page (https://www.facebook.com)
driver.get("http://qatechhub.com")  # Navigate back to the QA Tech Hub website.
print(driver.current_url)  # Print the URL of the current page.
driver.forward()  # Navigate forward.
driver.refresh()  # Reload the page.
driver.close()  # Close the Browser.












