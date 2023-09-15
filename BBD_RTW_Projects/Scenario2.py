from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

serviceobject = Service("C:\Pinky\PythonSelenium\drivers\msedgedriver.exe")
driver = webdriver.Edge(service=serviceobject)

# choptions = webdriver.ChromeOptions()
# choptions.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=choptions)

driver.maximize_window()
driver.get("https://in.yahoo.com/")

# Display the temperature at the current location
current_temp = driver.find_element(By.CSS_SELECTOR,".currentTemp").text
current_location = driver.find_element(By.CSS_SELECTOR,".city").text
print("Current temperature at " + current_location + " is " + current_temp)

#  Verify text "Trending Now"
TrendingNow = driver.find_element(By.XPATH,"//div/h3[contains(text(),'Trending now')]").text
assert "Trending now" in TrendingNow

# Get total number of links under Trending Now header and print the link text
link_list = driver.find_elements(By.XPATH,"//*/div[@class='c-list s-list-general D(n) srchActiveTab__D(b) Mt(4px) srchActiveTab']/descendant::a")
links_count = len(link_list)  # counts the number of item(webelements) in the list
#print(links_count)
link_text = driver.find_element(By.CSS_SELECTOR,".c-list").text
print("Following are the top " + str(links_count) + " trending searches in Yahoo: \n" + link_text)

# Navigate to each link and come back again to main page



