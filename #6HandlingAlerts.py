from selenium import webdriver
from selenium.webdriver.common.by import By

chromeoptionsobj = webdriver.ChromeOptions()
chromeoptionsobj.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chromeoptionsobj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#Pop-ups cannot be identified using inspect html
# So in this case we can assert that the correct text is displayed in the pop-up
name = "Pinky Kalita"
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"confirmbtn").click()

#Now we have to tell selenium to switch focus from browser to the alert pop-up using "switch_to" keyword
alertobj = driver.switch_to.alert  # alert object will focus only on the alert
alerttext = alertobj.text
assert name in alerttext
print(alerttext)

# to click OK button on the pop-up
alertobj.accept()

#to dismiss the alert pop-up
alertobj.dismiss()

driver.close()
