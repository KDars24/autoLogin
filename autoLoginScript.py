from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (change the path to where you saved the WebDriver)
# For windows check path of your broswer.
driver = webdriver.Chrome('/usr/bin/google-chrome')

# Navigate to the login page (replace with your actual login URL)
driver.get('192.168.222.111:1000')

# Wait for the username field to be visible
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'username'))
)

# Enter your credentials (replace with your actual username and password)
username_field.send_keys('your_username')


password_field = driver.find_element(By.ID, 'password')
password_field.send_keys('your_password')

# Submit the form
login_button = driver.find_element(By.ID, 'login_button')
login_button.click()

# Wait a few seconds for the login to complete
time.sleep(5)

# Close the browser
driver.quit()
