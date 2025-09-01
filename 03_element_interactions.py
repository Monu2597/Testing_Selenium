"""
Lesson 3: Basic Element Interactions
===================================

This lesson covers:
1. Click operations
2. Type operations
3. Clear operations
4. Submit operations
5. Get element properties
6. Element state checking

Key Concepts:
- Elements must be interactable before performing actions
- Always check element state before interaction
- Use appropriate wait strategies
- Handle different element types correctly
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

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

def demonstrate_click_operations(driver):
    """Demonstrate various click operations"""
    print("\n=== Click Operations ===")
    
    try:
        # Navigate to Google
        driver.get("https://www.google.com")
        wait = WebDriverWait(driver, 10)
        
        # Find search box
        search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        print("✓ Found search box")
        
        # Type text
        search_box.send_keys("Selenium testing")
        print("✓ Typed text in search box")
        
        # Click on search button
        search_button = wait.until(EC.element_to_be_clickable((By.NAME, "btnK")))
        search_button.click()
        print("✓ Clicked search button")
        
        time.sleep(3)
        
        # Click on first result
        first_result = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h3")))
        first_result.click()
        print("✓ Clicked on first search result")
        
        time.sleep(3)
        
    except Exception as e:
        print(f"❌ Click operations failed: {e}")

def demonstrate_type_operations(driver):
    """Demonstrate various typing operations"""
    print("\n=== Type Operations ===")
    
    try:
        # Navigate to Facebook
        driver.get("https://www.facebook.com")
        wait = WebDriverWait(driver, 10)
        
        # Find email field
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        print("✓ Found email field")
        
        # Type text
        email_field.send_keys("test@example.com")
        print("✓ Typed email address")
        
        # Clear and retype
        email_field.clear()
        print("✓ Cleared email field")
        email_field.send_keys("newemail@example.com")
        print("✓ Typed new email address")
        
        # Type with special keys
        email_field.send_keys(Keys.CONTROL + "a")  # Select all
        print("✓ Selected all text using Ctrl+A")
        email_field.send_keys(Keys.DELETE)  # Delete selected
        print("✓ Deleted selected text")
        email_field.send_keys("final@example.com")
        print("✓ Typed final email address")
        
        time.sleep(2)
        
    except Exception as e:
        print(f"❌ Type operations failed: {e}")

def demonstrate_clear_operations(driver):
    """Demonstrate clear operations"""
    print("\n=== Clear Operations ===")
    
    try:
        # Navigate to Amazon
        driver.get("https://www.amazon.com")
        wait = WebDriverWait(driver, 10)
        
        # Find search box
        search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
        print("✓ Found Amazon search box")
        
        # Type text
        search_box.send_keys("laptop computer")
        print("✓ Typed 'laptop computer' in search box")
        
        # Clear using clear() method
        search_box.clear()
        print("✓ Cleared search box using clear() method")
        
        # Verify it's empty
        if search_box.get_attribute("value") == "":
            print("✓ Search box is empty")
        else:
            print("❌ Search box is not empty")
        
        # Type new text
        search_box.send_keys("smartphone")
        print("✓ Typed 'smartphone' in search box")
        
        time.sleep(2)
        
    except Exception as e:
        print(f"❌ Clear operations failed: {e}")

def demonstrate_submit_operations(driver):
    """Demonstrate submit operations"""
    print("\n=== Submit Operations ===")
    
    try:
        # Navigate to Google
        driver.get("https://www.google.com")
        wait = WebDriverWait(driver, 10)
        
        # Find search form
        search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        print("✓ Found Google search box")
        
        # Type search query
        search_box.send_keys("Python programming")
        print("✓ Typed 'Python programming' in search box")
        
        # Submit the form
        search_box.submit()
        print("✓ Submitted search form")
        
        time.sleep(3)
        
        # Verify search results
        if "Python" in driver.title:
            print("✓ Search submitted successfully")
        else:
            print("❌ Search submission failed")
        
    except Exception as e:
        print(f"❌ Submit operations failed: {e}")

def demonstrate_element_properties(driver):
    """Demonstrate getting element properties"""
    print("\n=== Element Properties ===")
    
    try:
        # Navigate to a page
        driver.get("https://www.google.com")
        wait = WebDriverWait(driver, 10)
        
        # Find search box
        search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        print("✓ Found search box")
        
        # Get various properties
        tag_name = search_box.tag_name
        print(f"✓ Tag name: {tag_name}")
        
        element_type = search_box.get_attribute("type")
        print(f"✓ Element type: {element_type}")
        
        element_name = search_box.get_attribute("name")
        print(f"✓ Element name: {element_name}")
        
        element_id = search_box.get_attribute("id")
        print(f"✓ Element ID: {element_id}")
        
        element_class = search_box.get_attribute("class")
        print(f"✓ Element class: {element_class}")
        
        element_placeholder = search_box.get_attribute("placeholder")
        print(f"✓ Element placeholder: {element_placeholder}")
        
        # Get CSS properties
        font_size = search_box.value_of_css_property("font-size")
        print(f"✓ Font size: {font_size}")
        
        color = search_box.value_of_css_property("color")
        print(f"✓ Text color: {color}")
        
    except Exception as e:
        print(f"❌ Element properties failed: {e}")

def demonstrate_element_state_checking(driver):
    """Demonstrate checking element states"""
    print("\n=== Element State Checking ===")
    
    try:
        # Navigate to Facebook
        driver.get("https://www.facebook.com")
        wait = WebDriverWait(driver, 10)
        
        # Find email field
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        print("✓ Found email field")
        
        # Check if element is displayed
        if email_field.is_displayed():
            print("✓ Email field is displayed")
        else:
            print("❌ Email field is not displayed")
        
        # Check if element is enabled
        if email_field.is_enabled():
            print("✓ Email field is enabled")
        else:
            print("❌ Email field is not enabled")
        
        # Check if element is selected (for checkboxes/radio buttons)
        if email_field.is_selected():
            print("✓ Email field is selected")
        else:
            print("✓ Email field is not selected (expected for input field)")
        
        # Find password field
        password_field = driver.find_element(By.NAME, "pass")
        
        # Check if password field is displayed and enabled
        print(f"✓ Password field displayed: {password_field.is_displayed()}")
        print(f"✓ Password field enabled: {password_field.is_enabled()}")
        
        time.sleep(2)
        
    except Exception as e:
        print(f"❌ Element state checking failed: {e}")

def demonstrate_action_chains(driver):
    """Demonstrate ActionChains for complex interactions"""
    print("\n=== Action Chains ===")
    
    try:
        # Navigate to Google
        driver.get("https://www.google.com")
        wait = WebDriverWait(driver, 10)
        
        # Find search box
        search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        print("✓ Found search box")
        
        # Create ActionChains instance
        actions = ActionChains(driver)
        
        # Click and hold
        actions.click_and_hold(search_box).perform()
        print("✓ Clicked and held search box")
        
        # Release
        actions.release().perform()
        print("✓ Released search box")
        
        # Double click
        actions.double_click(search_box).perform()
        print("✓ Double clicked search box")
        
        # Type text
        search_box.send_keys("ActionChains demo")
        print("✓ Typed text using send_keys")
        
        # Select all text using ActionChains
        actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        print("✓ Selected all text using ActionChains")
        
        time.sleep(2)
        
    except Exception as e:
        print(f"❌ Action chains failed: {e}")

def demonstrate_form_handling(driver):
    """Demonstrate complete form handling"""
    print("\n=== Form Handling ===")
    
    try:
        # Navigate to a simple form page
        driver.get("https://www.google.com")
        wait = WebDriverWait(driver, 10)
        
        # Find search box
        search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        print("✓ Found search form")
        
        # Fill the form
        search_box.clear()
        search_box.send_keys("Selenium WebDriver tutorial")
        print("✓ Filled search form")
        
        # Submit the form
        search_box.submit()
        print("✓ Submitted search form")
        
        time.sleep(3)
        
        # Verify form submission
        if "Selenium" in driver.title:
            print("✓ Form submitted successfully")
        else:
            print("✓ Form submitted (title changed)")
        
        # Go back to search page
        driver.back()
        time.sleep(2)
        
        # Verify we're back
        if "Google" in driver.title:
            print("✓ Successfully returned to search page")
        
    except Exception as e:
        print(f"❌ Form handling failed: {e}")

def main():
    """Main function to demonstrate all element interactions"""
    print("=== Selenium Element Interactions Tutorial ===\n")
    
    try:
        driver = setup_driver()
        print("✓ WebDriver setup successful!")
        
        # Demonstrate all interaction types
        demonstrate_click_operations(driver)
        demonstrate_type_operations(driver)
        demonstrate_clear_operations(driver)
        demonstrate_submit_operations(driver)
        demonstrate_element_properties(driver)
        demonstrate_element_state_checking(driver)
        demonstrate_action_chains(driver)
        demonstrate_form_handling(driver)
        
        print("\n" + "="*60)
        print("✓ All element interactions demonstrated successfully!")
        print("\nKey Takeaways:")
        print("- Always check element state before interaction")
        print("- Use appropriate wait strategies")
        print("- Clear fields before typing new content")
        print("- Use submit() for form submission")
        print("- ActionChains for complex interactions")
        print("- Check element properties for validation")
        
    except Exception as e:
        print(f"❌ Tutorial failed: {e}")
    
    finally:
        if 'driver' in locals():
            print("\nClosing browser...")
            driver.quit()

if __name__ == "__main__":
    main()
