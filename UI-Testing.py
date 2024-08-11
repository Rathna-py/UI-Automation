import os
import time
from datetime import datetime
from selenium import webdriver

# URLs to be tested (add all URLs from your sitemap)
urls = ["https://www.getcalley.com/page1", "https://www.getcalley.com/page2", "https://www.getcalley.com/calley-pro-features/", "https://www.getcalley.com/best-auto-dialer-app/", "https://www.getcalley.com/how-calley-auto-dialer-app-works/"]

# Resolutions and Devices
resolutions = {
    "Desktop": [(1920, 1080), (1366, 768), (1536, 864)],
    "Mobile": [(360, 640), (414, 896), (375, 667)]
}

# Browser setup (example for Chrome)
chrome_driver = webdriver.Chrome()

# Base directory for screenshots
base_directory = "D:/Python-Test/"

# Iterate over devices, resolutions, and URLs
for device, res_list in resolutions.items():
    for resolution in res_list:
        width, height = resolution
        for url in urls:
            # Set the window size to the current resolution
            chrome_driver.set_window_size(width, height)
            
            # Open the URL
            chrome_driver.get(url)
            
            # Allow some time for the page to load
            time.sleep(2)
            
            # Create directory for screenshots if it doesn't exist
            directory = f"{base_directory}/{device}/{width}x{height}"
            if not os.path.exists(directory):
                os.makedirs(directory)
                print(f"Created directory: {directory}")
            
            # Save the screenshot
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            screenshot_path = f"{directory}/Screenshot-{timestamp}.png"
            chrome_driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved: {screenshot_path}")

# Quit the browser
chrome_driver.quit()

# Browser setup (example for Firefox)
firefox_driver = webdriver.Firefox()

for device, res_list in resolutions.items():
    for resolution in res_list:
        width, height = resolution
        for url in urls:
            # Set the window size to the current resolution
            firefox_driver.set_window_size(width, height)
            
            # Open the URL
            firefox_driver.get(url)
            
            # Allow some time for the page to load
            time.sleep(2)
            
            # Create directory for screenshots if it doesn't exist
            directory = f"Firefox/{device}/{width}x{height}"
            if not os.path.exists(directory):
                os.makedirs(directory)
            
            # Save the screenshot
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            screenshot_path = f"{directory}/Screenshot-{timestamp}.png"
            firefox_driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved: {screenshot_path}")

# Quit the browser
firefox_driver.quit()
