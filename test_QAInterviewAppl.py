"""
SCOPE:
1) Launch browser
2) Navigate to http://qainterview.pythonanywhere.com/
3) Find elements using id, xpath..
4) Input the value 5 ,click on Calculate button  and check whether calculated factorial value is 120
5) Close the browser
"""
import time
from selenium import webdriver

desired_cap = { 'device': 'iPhone 7','realMobile': 'true', 'platform': 'iOS','browserName': 'safari', 'browserstack.debug': 'true' }
driver = webdriver.Remote(command_executor='http://sharadag1:ve5y9kXqdCoseBQYsxQ9@hub.browserstack.com:80/wd/hub',desired_capabilities=desired_cap)    


# Create an instance of Firefox WebDriver
#driver = webdriver.Chrome()

# The driver.get method will navigate to a page given by the URL
driver.get("https://qainterview.pythonanywhere.com/")

# Check if the title of the page is proper
if(driver.title=="Factoriall"):
    print ("Success: QA Interview Application page launched successfully")
else:
    print ("Failure: QA Interview Application page Title is incorrect")       

driver.find_element_by_xpath("//input[@id='number']").send_keys('5')

# Click Calculate Button
driver.find_element_by_id('getFactorial').click()

time.sleep(5)

result = float((driver.find_element_by_xpath("//p[@id='resultDiv']").text).split(':')[1].strip())

if ( result == 120):
    print("Result for 5! is correct:",result)
else:
    print("Result for 5! is incorrect:",result)

# Close the browser window
driver.close() 
        

