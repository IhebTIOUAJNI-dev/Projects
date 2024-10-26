from selenium import webdriver

# Specify the path to the chromedriver if it's not in your PATH
driver_path = 'C:\Program Files\Google\Chrome\Application\chrome'

# Initialize the WebDriver (in this case, Chrome)
driver = webdriver.Chrome(executable_path=driver_path)

# Open a webpage
driver.get('website')

# Print the title of the webpage
#print(driver.title)

# Close the browser
#driver.quit()

# Find an element by its ID and input text
search_box = driver.find_element_by_id('left-area')
search_box.send_keys('Selenium')

# Find a button by its XPATH and click it
search_button = driver.find_element_by_xpath('//button[@type="submit"]')
search_button.click()

# Wait for elements to load
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "someId"))
)

# Getting text from a web element
print(element.text)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "dynamicElement"))
    )
    print(element.text)
finally:
    driver.quit()
