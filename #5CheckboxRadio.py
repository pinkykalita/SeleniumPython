from selenium import webdriver
from selenium.webdriver.common.by import By

optionobj = webdriver.ChromeOptions()
optionobj.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=optionobj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# we can directly click on a checkbox with Id, Name, Text etc.
# But to do it dynamically, we can store the list of checkboxes in a list and then iterate through it and click on the needed checkbox

driver.find_element(By.CSS_SELECTOR,"#checkBoxOption1").click()  # select 1st checkbox

checkboxes = driver.find_elements(By.XPATH,"//fieldset[contains(.,'Checkbox Example')]/label/input")
print("There are "+ str(len(checkboxes)) + " checkboxes")
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()  # to assert if checkbox has been clicked
        break

# handling radio buttons
radiobuttons = driver.find_elements(By.XPATH,"//fieldset[contains(.,'Radio Button Example')]/label/input")
print("There are "+ str(len(checkboxes)) + " radio buttons")
for radiobtn in radiobuttons:
    if radiobtn.get_attribute("value") == "radio1":  # click radio btn 1
        radiobtn.click()
        print("radio button 1 selected")
        assert radiobtn.is_selected()
        break
radiobuttons[2].click()  # clicks the radio btn at index 2 (radio btn 3)

assert radiobuttons[2].is_selected()
print("radio button 3 selected")

# assert using is_displayed
assert driver.find_element(By.CSS_SELECTOR,"#displayed-text").is_displayed()  # this will return TRUE if the webelement is displayed
driver.find_element(By.CSS_SELECTOR,"#hide-textbox").click()  # on clicking the Hide btn, the textbox wll be not displayed on the screen
# assert driver.find_element(By.CSS_SELECTOR,"displayed-text").is_displayed()  # now running this will throe Assertion error, as the txtbox has been hidden
assert not driver.find_element(By.CSS_SELECTOR,"#displayed-text").is_displayed()  # assert not will throw no error if the webelemt returns Fa;se value



driver.close()

