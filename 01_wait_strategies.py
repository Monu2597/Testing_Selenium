"""
Lesson 4: Wait Strategies
=========================

This lesson covers:
1. Implicit Wait
2. Explicit Wait
3. Fluent Wait
4. Expected Conditions
5. Custom wait conditions
6. When to use each wait type

Key Concepts:
- Implicit wait: Global wait for all elements
- Explicit wait: Wait for specific conditions
- Fluent wait: Configurable explicit wait
- Always use explicit waits for dynamic elements
- Avoid Thread.sleep() in production code
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
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

def demonstrate_implicit_wait(driver):
    """Demonstrate implicit wait strategy"""
    print("\n=== Implicit Wait Strategy ===")
    
    try:
        # Set implicit wait to 10 seconds
        driver.implicitly_wait(10)
        print("✓ Set implicit wait to 10 seconds")
        
        # Navigate to a page
        driver.get("https://www.google.com")
        print("✓ Navigated to Google")
        
        # Try to find element (implicit wait will be applied)
        start_time = time.time()
        search_box = driver.find_element(By.NAME, "q")
        end_time = time.time()
        
        print(f"✓ Found search box in {end_time - start_time:.2f} seconds")
        print("✓ Implicit wait worked automatically")
        
        # Clear implicit wait
        driver.implicitly_wait(0)
        print("✓ Cleared implicit wait")
        
    except Exception as e:
        print(f"❌ Implicit wait failed: {e}")

def demonstrate_explicit_wait(driver):
    """Demonstrate explicit wait strategy"""
    print("\n=== Explicit Wait Strategy ===")
    
    try:
        # Navigate to Google
        driver.get("https://www.google.com")
        print("✓ Navigated to Google")
        
        # Create explicit wait with 10 second timeout
        wait = WebDriverWait(driver, 10)
        print("✓ Created explicit wait with 10 second timeout")
        
        # Wait for element to be present
        start_time = time.time()
        search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        end_time = time.time()
        
        print(f"✓ Element found in {end_time - start_time:.2f} seconds")
        print("✓ Explicit wait for presence successful")
        
        # Wait for element to be clickable
        start_time = time.time()
        search_button = wait.until(EC.element_to_be_clickable((By.NAME, "btnK")))
        end_time = time.time()
        
        print(f"✓ Button became clickable in {end_time - start_time:.2f} seconds")
        print("✓ Explicit wait for clickability successful")
        
        # Type in search box
        search_box.send_keys("explicit wait demo")
        print("✓ Typed text in search box")
        
    except Exception as e:
        print(f"❌ Explicit wait failed: {e}")

def demonstrate_fluent_wait(driver):
    """Demonstrate fluent wait strategy"""
    print("\n=== Fluent Wait Strategy ===")
    
    try:
        # Navigate to Facebook
        driver.get("https://www.facebook.com")
        print("✓ Navigated to Facebook")
        
        # Create fluent wait with custom polling
        wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)
        print("✓ Created fluent wait with 0.5 second polling")
        
        # Wait for email field with custom message
        start_time = time.time()
        email_field = wait.until(
            EC.presence_of_element_located((By.NAME, "email")),
            message="Email field not found within 10 seconds"
        )
        end_time = time.time()
        
        print(f"✓ Email field found in {end_time - start_time:.2f} seconds")
        print("✓ Fluent wait with custom polling successful")
        
        # Wait for password field
        password_field = wait.until(
            EC.presence_of_element_located((By.NAME, "pass")),
            message="Password field not found within 10 seconds"
        )
        print("✓ Password field found")
        
    except Exception as e:
        print(f"❌ Fluent wait failed: {e}")

def demonstrate_expected_conditions(driver):
    """Demonstrate various expected conditions"""
    print("\n=== Expected Conditions ===")
    
    try:
        # Navigate to Amazon
        driver.get("https://www.amazon.com")
        wait = WebDriverWait(driver, 10)
        print("✓ Navigated to Amazon")
        
        # Wait for title to contain specific text
        wait.until(EC.title_contains("Amazon"))
        print("✓ Title contains 'Amazon'")
        
        # Wait for URL to contain specific text
        wait.until(EC.url_contains("amazon"))
        print("✓ URL contains 'amazon'")
        
        # Wait for page to load completely
        wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
        print("✓ Page loaded completely")
        
        # Wait for search box to be visible
        search_box = wait.until(EC.visibility_of_element_located((By.ID, "twotabsearchtextbox")))
        print("✓ Search box is visible")
        
        # Wait for element to be present in DOM
        wait.until(EC.presence_of_element_located((By.ID, "nav-main")))
        print("✓ Navigation menu is present in DOM")
        
        # Wait for element to be clickable
        wait.until(EC.element_to_be_clickable((By.ID, "nav-search-submit-button")))
        print("✓ Search button is clickable")
        
    except Exception as e:
        print(f"❌ Expected conditions failed: {e}")

def demonstrate_custom_wait_conditions(driver):
    """Demonstrate custom wait conditions"""
    print("\n=== Custom Wait Conditions ===")
    
    try:
        # Navigate to Google
        driver.get("https://www.google.com")
        wait = WebDriverWait(driver, 10)
        print("✓ Navigated to Google")
        
        # Custom condition: Wait for element to have specific text
        def element_has_text(locator, text):
            def condition(driver):
                element = driver.find_element(*locator)
                return text in element.get_attribute("value")
            return condition
        
        # Wait for search box to have placeholder text
        wait.until(element_has_text((By.NAME, "q"), "Google"))
        print("✓ Search box has placeholder text")
        
        # Custom condition: Wait for page to have specific number of links
        def page_has_minimum_links(min_links):
            def condition(driver):
                links = driver.find_elements(By.TAG_NAME, "a")
                return len(links) >= min_links
            return condition
        
        # Wait for page to have at least 10 links
        wait.until(page_has_minimum_links(10))
        print("✓ Page has at least 10 links")
        
        # Custom condition: Wait for element to be enabled and visible
        def element_is_enabled_and_visible(locator):
            def condition(driver):
                element = driver.find_element(*locator)
                return element.is_enabled() and element.is_displayed()
            return condition
        
        # Wait for search box to be enabled and visible
        wait.until(element_is_enabled_and_visible((By.NAME, "q")))
        print("✓ Search box is enabled and visible")
        
    except Exception as e:
        print(f"❌ Custom wait conditions failed: {e}")

def demonstrate_wait_timeout_handling(driver):
    """Demonstrate handling wait timeouts"""
    print("\n=== Wait Timeout Handling ===")
    
    try:
        # Navigate to Google
        driver.get("https://www.google.com")
        print("✓ Navigated to Google")
        
        # Create wait with short timeout to demonstrate timeout
        short_wait = WebDriverWait(driver, 2)
        print("✓ Created wait with 2 second timeout")
        
        # Try to find non-existent element
        try:
            non_existent = short_wait.until(EC.presence_of_element_located((By.ID, "non-existent-id")))
            print("❌ Unexpected: Element found")
        except TimeoutException:
            print("✓ Expected: TimeoutException caught for non-existent element")
        
        # Try to find element that exists
        try:
            search_box = short_wait.until(EC.presence_of_element_located((By.NAME, "q")))
            print("✓ Element found within timeout")
        except TimeoutException:
            print("❌ Unexpected: TimeoutException for existing element")
        
        # Demonstrate different timeout scenarios
        print("\nDemonstrating different wait scenarios:")
        
        # Wait for element to be clickable
        wait = WebDriverWait(driver, 10)
        search_button = wait.until(EC.element_to_be_clickable((By.NAME, "btnK")))
        print("✓ Search button is clickable")
        
        # Wait for element to be selected (will timeout for input field)
        try:
            wait.until(EC.element_to_be_selected((By.NAME, "q")))
            print("❌ Unexpected: Input field should not be selectable")
        except TimeoutException:
            print("✓ Expected: TimeoutException for non-selectable element")
        
    except Exception as e:
        print(f"❌ Wait timeout handling failed: {e}")

def demonstrate_wait_best_practices(driver):
    """Demonstrate wait best practices"""
    print("\n=== Wait Best Practices ===")
    
    try:
        # Navigate to a page
        driver.get("https://www.google.com")
        print("✓ Navigated to Google")
        
        # Best Practice 1: Use explicit waits instead of implicit waits
        wait = WebDriverWait(driver, 10)
        print("✓ Using explicit wait instead of implicit wait")
        
        # Best Practice 2: Wait for specific conditions, not just presence
        search_box = wait.until(EC.element_to_be_clickable((By.NAME, "q")))
        print("✓ Waited for element to be clickable, not just present")
        
        # Best Practice 3: Use meaningful timeout values
        reasonable_timeout = WebDriverWait(driver, 10)
        print("✓ Using reasonable timeout (10 seconds)")
        
        # Best Practice 4: Handle timeouts gracefully
        try:
            element = reasonable_timeout.until(EC.presence_of_element_located((By.NAME, "q")))
            print("✓ Element found successfully")
        except TimeoutException:
            print("❌ Element not found within timeout")
            # Handle the timeout appropriately
        
        # Best Practice 5: Wait for page load completion
        wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
        print("✓ Waited for page to load completely")
        
        # Best Practice 6: Use specific locators
        specific_element = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        print("✓ Used specific locator (name='q')")
        
        print("\n✓ Best practices demonstrated:")
        print("  - Use explicit waits over implicit waits")
        print("  - Wait for specific conditions")
        print("  - Use reasonable timeout values")
        print("  - Handle timeouts gracefully")
        print("  - Wait for page load completion")
        print("  - Use specific and stable locators")
        
    except Exception as e:
        print(f"❌ Wait best practices failed: {e}")

def main():
    """Main function to demonstrate all wait strategies"""
    print("=== Selenium Wait Strategies Tutorial ===\n")
    
    try:
        driver = setup_driver()
        print("✓ WebDriver setup successful!")
        
        # Demonstrate all wait strategies
        demonstrate_implicit_wait(driver)
        demonstrate_explicit_wait(driver)
        demonstrate_fluent_wait(driver)
        demonstrate_expected_conditions(driver)
        demonstrate_custom_wait_conditions(driver)
        demonstrate_wait_timeout_handling(driver)
        demonstrate_wait_best_practices(driver)
        
        print("\n" + "="*60)
        print("✓ All wait strategies demonstrated successfully!")
        print("\nKey Takeaways:")
        print("- Implicit wait: Global, simple, but less reliable")
        print("- Explicit wait: Specific, reliable, recommended for production")
        print("- Fluent wait: Configurable explicit wait with custom polling")
        print("- Always use explicit waits for dynamic elements")
        print("- Handle timeouts gracefully")
        print("- Use appropriate expected conditions")
        print("- Avoid Thread.sleep() in production code")
        
    except Exception as e:
        print(f"❌ Tutorial failed: {e}")
    
    finally:
        if 'driver' in locals():
            print("\nClosing browser...")
            driver.quit()

if __name__ == "__main__":
    main()
