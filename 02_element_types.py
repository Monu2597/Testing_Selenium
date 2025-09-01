"""
Lesson 5: Handling Different Element Types
=========================================

This lesson covers:
1. Dropdown/Select elements
2. Checkboxes and Radio buttons
3. Iframes and Frames
4. Tables
5. Alerts and Popups
6. File uploads
7. Dynamic elements

Key Concepts:
- Different element types require different handling approaches
- Use Select class for dropdowns
- Handle iframes by switching context
- Always check element state before interaction
- Use appropriate wait strategies for dynamic elements
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

def setup_driver():
    """Setup Chrome WebDriver"""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    chrome_service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    return driver

def demonstrate_dropdown_handling(driver):
    """Demonstrate handling dropdown/select elements"""
    print("\n=== Dropdown/Select Element Handling ===")
    
    try:
        # Navigate to a page with dropdowns (using a demo page)
        driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")
        wait = WebDriverWait(driver, 10)
        print("✓ Navigated to dropdown demo page")
        
        # Find the dropdown element
        dropdown = wait.until(EC.presence_of_element_located((By.ID, "select-demo")))
        print("✓ Found dropdown element")
        
        # Create Select object
        select = Select(dropdown)
        print("✓ Created Select object")
        
        # Get all options
        options = select.options
        print(f"✓ Found {len(options)} options in dropdown")
        
        # Get first option text
        first_option = options[0].text
        print(f"✓ First option: {first_option}")
        
        # Select by visible text
        select.select_by_visible_text("Sunday")
        print("✓ Selected 'Sunday' by visible text")
        
        # Get selected option
        selected_option = select.first_selected_option
        print(f"✓ Currently selected: {selected_option.text}")
        
        # Select by value
        select.select_by_value("Monday")
        print("✓ Selected 'Monday' by value")
        
        # Select by index
        select.select_by_index(2)  # Tuesday
        print("✓ Selected option at index 2")
        
        # Check if multiple selection is allowed
        is_multiple = select.is_multiple
        print(f"✓ Multiple selection allowed: {is_multiple}")
        
        time.sleep(2)
        
    except Exception as e:
        print(f"❌ Dropdown handling failed: {e}")

def demonstrate_checkbox_radio_handling(driver):
    """Demonstrate handling checkboxes and radio buttons"""
    print("\n=== Checkbox and Radio Button Handling ===")
    
    try:
        # Navigate to a page with checkboxes and radio buttons
        driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")
        wait = WebDriverWait(driver, 10)
        print("✓ Navigated to checkbox demo page")
        
        # Find checkboxes
        checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        print(f"✓ Found {len(checkboxes)} checkboxes")
        
        # Check first checkbox
        if checkboxes:
            first_checkbox = checkboxes[0]
            if not first_checkbox.is_selected():
                first_checkbox.click()
                print("✓ Clicked first checkbox")
            else:
                print("✓ First checkbox was already selected")
            
            # Verify selection
            if first_checkbox.is_selected():
                print("✓ First checkbox is now selected")
            else:
                print("❌ First checkbox selection failed")
        
        # Navigate to radio button demo
        driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")
        wait.until(EC.presence_of_element_located((By.NAME, "optradio")))
        print("✓ Navigated to radio button demo page")
        
        # Find radio buttons
        radio_buttons = driver.find_elements(By.NAME, "optradio")
        print(f"✓ Found {len(radio_buttons)} radio buttons")
        
        # Select first radio button
        if radio_buttons:
            first_radio = radio_buttons[0]
            first_radio.click()
            print("✓ Clicked first radio button")
            
            # Verify selection
            if first_radio.is_selected():
                print("✓ First radio button is selected")
            else:
                print("❌ First radio button selection failed")
        
        time.sleep(2)
        
    except Exception as e:
        print(f"❌ Checkbox/Radio handling failed: {e}")

def demonstrate_iframe_handling(driver):
    """Demonstrate handling iframes and frames"""
    print("\n=== Iframe and Frame Handling ===")
    
    try:
        # Navigate to a page with iframes
        driver.get("https://www.seleniumeasy.com/test/iframe-practice-page.html")
        wait = WebDriverWait(driver, 10)
        print("✓ Navigated to iframe demo page")
        
        # Find iframes
        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        print(f"✓ Found {len(iframes)} iframes on the page")
        
        # Switch to first iframe
        if iframes:
            driver.switch_to.frame(iframes[0])
            print("✓ Switched to first iframe")
            
            # Find elements inside iframe
            iframe_content = driver.find_element(By.TAG_NAME, "body")
            print(f"✓ Found iframe content: {iframe_content.text[:50]}...")
            
            # Switch back to main content
            driver.switch_to.default_content()
            print("✓ Switched back to main content")
        
        # Switch to iframe by index
        driver.switch_to.frame(0)
        print("✓ Switched to iframe by index 0")
        
        # Switch back to main content
        driver.switch_to.default_content()
        print("✓ Switched back to main content")
        
        # Switch to iframe by name (if available)
        try:
            driver.switch_to.frame("iframe-name")
            print("✓ Switched to iframe by name")
            driver.switch_to.default_content()
        except:
            print("✓ Iframe by name not available")
        
        time.sleep(2)
        
    except Exception as e:
        print(f"❌ Iframe handling failed: {e}")

def demonstrate_table_handling(driver):
    """Demonstrate handling table elements"""
    print("\n=== Table Element Handling ===")
    
    try:
        # Navigate to a page with tables
        driver.get("https://www.seleniumeasy.com/test/table-data-download-demo.html")
        wait = WebDriverWait(driver, 10)
        print("✓ Navigated to table demo page")
        
        # Find table
        table = wait.until(EC.presence_of_element_located((By.ID, "example")))
        print("✓ Found table element")
        
        # Find table rows
        rows = table.find_elements(By.TAG_NAME, "tr")
        print(f"✓ Found {len(rows)} rows in table")
        
        # Find table headers
        headers = rows[0].find_elements(By.TAG_NAME, "th")
        print(f"✓ Found {len(headers)} columns in table")
        
        # Print header names
        header_names = [header.text for header in headers]
        print(f"✓ Table headers: {header_names}")
        
        # Find specific row by text
        target_row = None
        for row in rows[1:]:  # Skip header row
            cells = row.find_elements(By.TAG_NAME, "td")
            if cells and "Software Engineer" in cells[1].text:
                target_row = row
                break
        
        if target_row:
            print("✓ Found row containing 'Software Engineer'")
            cells = target_row.find_elements(By.TAG_NAME, "td")
            print(f"✓ Row data: {[cell.text for cell in cells]}")
        
        # Find all cells in a specific column
        if len(rows) > 1:
            name_column = []
            for row in rows[1:]:  # Skip header row
                cells = row.find_elements(By.TAG_NAME, "td")
                if cells:
                    name_column.append(cells[0].text)
            print(f"✓ Names in first column: {name_column[:5]}...")  # Show first 5
        
        time.sleep(2)
        
    except Exception as e:
        print(f"❌ Table handling failed: {e}")

def demonstrate_alert_popup_handling(driver):
    """Demonstrate handling alerts and popups"""
    print("\n=== Alert and Popup Handling ===")
    
    try:
        # Navigate to a page with alerts
        driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
        wait = WebDriverWait(driver, 10)
        print("✓ Navigated to alert demo page")
        
        # Find alert button
        alert_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-default")))
        print("✓ Found alert button")
        
        # Click button to trigger alert
        alert_button.click()
        print("✓ Clicked alert button")
        
        # Wait for alert and switch to it
        alert = wait.until(EC.alert_is_present())
        print("✓ Alert appeared")
        
        # Get alert text
        alert_text = alert.text
        print(f"✓ Alert text: {alert_text}")
        
        # Accept alert
        alert.accept()
        print("✓ Accepted alert")
        
        # Find confirm button
        confirm_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='myConfirmFunction()']")
        print("✓ Found confirm button")
        
        # Click confirm button
        confirm_button.click()
        print("✓ Clicked confirm button")
        
        # Wait for confirm dialog
        confirm_alert = wait.until(EC.alert_is_present())
        print("✓ Confirm dialog appeared")
        
        # Dismiss confirm dialog
        confirm_alert.dismiss()
        print("✓ Dismissed confirm dialog")
        
        time.sleep(2)
        
    except Exception as e:
        print(f"❌ Alert handling failed: {e}")

def demonstrate_file_upload(driver):
    """Demonstrate file upload handling"""
    print("\n=== File Upload Handling ===")
    
    try:
        # Navigate to a page with file upload
        driver.get("https://www.seleniumeasy.com/test/generate-file-to-download-demo.html")
        wait = WebDriverWait(driver, 10)
        print("✓ Navigated to file upload demo page")
        
        # Find text area for file content
        text_area = wait.until(EC.presence_of_element_located((By.ID, "textbox")))
        print("✓ Found text area")
        
        # Enter some text
        text_area.clear()
        text_area.send_keys("This is a test file content for Selenium automation testing.")
        print("✓ Entered text in text area")
        
        # Find generate file button
        generate_button = driver.find_element(By.ID, "create")
        print("✓ Found generate file button")
        
        # Click generate button
        generate_button.click()
        print("✓ Clicked generate file button")
        
        # Find download link
        download_link = wait.until(EC.element_to_be_clickable((By.ID, "link-to-download")))
        print("✓ Found download link")
        
        # Get download URL
        download_url = download_link.get_attribute("href")
        print(f"✓ Download URL: {download_url}")
        
        time.sleep(2)
        
    except Exception as e:
        print(f"❌ File upload handling failed: {e}")

def demonstrate_dynamic_elements(driver):
    """Demonstrate handling dynamic elements"""
    print("\n=== Dynamic Element Handling ===")
    
    try:
        # Navigate to a page with dynamic content
        driver.get("https://www.seleniumeasy.com/test/dynamic-data-loading-demo.html")
        wait = WebDriverWait(driver, 10)
        print("✓ Navigated to dynamic content demo page")
        
        # Find get new user button
        get_user_button = wait.until(EC.element_to_be_clickable((By.ID, "save")))
        print("✓ Found get new user button")
        
        # Click button to load dynamic content
        get_user_button.click()
        print("✓ Clicked get new user button")
        
        # Wait for dynamic content to load
        dynamic_content = wait.until(EC.presence_of_element_located((By.ID, "loading")))
        print("✓ Dynamic content started loading")
        
        # Wait for loading to complete (content becomes visible)
        wait.until(EC.invisibility_of_element_located((By.ID, "loading")))
        print("✓ Dynamic content loaded")
        
        # Get the loaded content
        user_info = driver.find_element(By.CSS_SELECTOR, "#loading img")
        if user_info.is_displayed():
            print("✓ User image loaded successfully")
        
        # Find user details
        user_details = driver.find_elements(By.CSS_SELECTOR, "#loading p")
        if user_details:
            print(f"✓ Found {len(user_details)} user detail lines")
            for detail in user_details:
                if detail.text.strip():
                    print(f"  - {detail.text}")
        
        time.sleep(2)
        
    except Exception as e:
        print(f"❌ Dynamic element handling failed: {e}")

def demonstrate_element_verification(driver):
    """Demonstrate verifying element states and properties"""
    print("\n=== Element Verification ===")
    
    try:
        # Navigate to a simple page
        driver.get("https://www.google.com")
        wait = WebDriverWait(driver, 10)
        print("✓ Navigated to Google")
        
        # Find search box
        search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        print("✓ Found search box")
        
        # Verify element properties
        print(f"✓ Element tag: {search_box.tag_name}")
        print(f"✓ Element type: {search_box.get_attribute('type')}")
        print(f"✓ Element name: {search_box.get_attribute('name')}")
        print(f"✓ Element placeholder: {search_box.get_attribute('placeholder')}")
        
        # Verify element state
        print(f"✓ Element displayed: {search_box.is_displayed()}")
        print(f"✓ Element enabled: {search_box.is_enabled()}")
        print(f"✓ Element selected: {search_box.is_selected()}")
        
        # Verify element size and position
        size = search_box.size
        location = search_box.location
        print(f"✓ Element size: {size['width']}x{size['height']}")
        print(f"✓ Element location: ({location['x']}, {location['y']})")
        
        # Verify CSS properties
        font_size = search_box.value_of_css_property("font-size")
        color = search_box.value_of_css_property("color")
        print(f"✓ Element font size: {font_size}")
        print(f"✓ Element text color: {color}")
        
    except Exception as e:
        print(f"❌ Element verification failed: {e}")

def main():
    """Main function to demonstrate all element type handling"""
    print("=== Selenium Element Types Handling Tutorial ===\n")
    
    try:
        driver = setup_driver()
        print("✓ WebDriver setup successful!")
        
        # Demonstrate all element type handling
        demonstrate_dropdown_handling(driver)
        demonstrate_checkbox_radio_handling(driver)
        demonstrate_iframe_handling(driver)
        demonstrate_table_handling(driver)
        demonstrate_alert_popup_handling(driver)
        demonstrate_file_upload(driver)
        demonstrate_dynamic_elements(driver)
        demonstrate_element_verification(driver)
        
        print("\n" + "="*60)
        print("✓ All element types handled successfully!")
        print("\nKey Takeaways:")
        print("- Use Select class for dropdown elements")
        print("- Check element state before interaction")
        print("- Switch to iframes to interact with their content")
        print("- Handle dynamic elements with appropriate waits")
        print("- Verify element properties and states")
        print("- Use proper locators for different element types")
        print("- Handle alerts and popups carefully")
        
    except Exception as e:
        print(f"❌ Tutorial failed: {e}")
    
    finally:
        if 'driver' in locals():
            print("\nClosing browser...")
            driver.quit()

if __name__ == "__main__":
    main()
