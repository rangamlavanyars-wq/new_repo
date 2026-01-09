'''Challenge 1: Basic Login Form
Scenario: Automate login to a website with username and password fields. Verify successful login by
checking for a welcome message.
'''

from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()

driver.get('https://automation-practice-website.onrender.com/')
sleep(2)
driver.find_element('xpath','//a[@href="/forms"]').click()
name=(driver.find_element('id','name'))
name.send_keys('lavanya')
driver.find_element('id','email').send_keys('lavanya@gmail.com')
driver.find_element('id','password').send_keys('123456789')
expected_value=name.get_attribute('value')
alert_successful=driver.find_element('xpath','//button[.="Login"]')
alert_successful.click()
alert_obj=driver.switch_to.alert
actual_text=alert_obj.text
alert_obj.accept()

assert expected_value in actual_text , f'Login not Successful expected value is {expected_value} but actual value is {actual_text}'
print('Login Successful!')

'''Challenge 2: Handling Dynamic Wait
Scenario: Navigate to a page with a button that, when clicked, displays a message after a random delay
(1-5 seconds). Implement appropriate waits to verify the message appears.
'''
# from time import sleep
# from selenium import webdriver

'''Challenge 4: Table Data Extraction
Scenario: From a webpage containing a table with multiple rows and columns, extract all data and store
it in a structured format (e.g., list of dictionaries).
'''



    