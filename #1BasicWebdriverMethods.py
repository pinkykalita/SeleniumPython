from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Service() # import service class
#service_obj = Service()  # create an object for Service class, without chromedriver installed locally
Serviceobj = Service("C:\Pinky\PythonSelenium\drivers\chromedriver.exe") # passing chromedriver local path
driver = webdriver.Chrome(service=Serviceobj)
#driver = webdriver.Chrome()  # initilizing/invoke the web driver
driver.maximize_window()  # maximize the window
driver.get("https://www.lambdatest.com/blog/selenium-python-cheat-sheet/")  # open the website
print("opening " + driver.name + " browser")  # prints name of the browsers
s1 = driver.title  # get the page title
print("the title of the page is: " + s1)
s2 = driver.current_url  # gets the current url where we landed
print(s2)  # prints the current url on the console
driver.get("https://accounts.lambdatest.com/login?_gl=1*mgilef*_gcl_au*MTkzMzA3MjY5My4xNjkyMzM5MjI4")
driver.minimize_window()  # this will minimize the window
driver.back()   # go back to the lamdatest Home screen
print(driver.title)
driver.forward()  # go to Login screen again
print(driver.title)


driver = webdriver.Edge()
driver.get("https://www.javatpoint.com/selenium-webdriver-commands")
print("opening " + driver.name + " browser")  # prints name of the browsers

#driver = webdriver.Firefox()
Serviceobj1 = Service("C:\Pinky\PythonSelenium\drivers\geckodriver.exe") # passing chromedriver local path
driver = webdriver.Firefox(service=Serviceobj1)
driver.get("https://selenium-python.readthedocs.io/navigating.html")
print("opening " + driver.name + " browser")  # prints name of the browsers

#driver = webdriver.Safari()
#driver.get("https://www.lambdatest.com/blog/selenium-python-cheat-sheet/")
#print(driver.name) # prints name of the browsers


driver.close()  # close the browser