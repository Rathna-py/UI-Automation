import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Replace with your actual details
login_url = "https://demo.dealsdray.com/"
username = "prexo.mis@dealsdray.com"
password = "prexo.mis@dealsdray.com"
upload_url = "//*[@id='mui-11']"
xls_file_path = "C:/Users/gohul/Downloads/demo-data.xlsx"

driver = webdriver.Chrome()

start_time = datetime.now()
driver.get(login_url)
time.sleep(2)
driver.maximize_window()
driver.find_element(By.XPATH, "//*[@id='mui-1']").send_keys(username)
driver.find_element(By.XPATH, "//*[@id='mui-2']").send_keys(password)
driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div[2]/div/form/div[3]/div/button").click()
time.sleep(3)

driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div/div[2]/div[1]/div[2]/button/div[2]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/a/button").click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[contains(text(),'Add Bulk Orders')]").click()
time.sleep(3)

# Step 4: Upload the XLS File
driver.find_element(By.XPATH, "//input[@id='mui-11']").send_keys(xls_file_path)
time.sleep(5)
driver.find_element(By.XPATH, "//button[contains(text(),'Import')]").click()
time.sleep(3)  # Wait for the upload to complete

# Step 5: Perform Validations
driver.find_element(By.XPATH, "//button[contains(text(),'Validate Data')]").click()

# Step 6: Take a Screenshot
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
screenshot_path = f"screenshot-{timestamp}.png"
driver.save_screenshot(screenshot_path)
print(f"Screenshot saved: {screenshot_path}")


# End the script and record the time
end_time = datetime.now()
duration = end_time - start_time
print(f"Test completed in: {duration}")

# Quit the browser
driver.quit()