"""
Lesson 2: Element Location Strategies
====================================

This lesson covers:
1. ID locator
2. Name locator
3. Class name locator
4. Tag name locator
5. Link text and partial link text
6. CSS selector
7. XPath

Key Concepts:
- Locators are used to find elements on a web page
- Each locator type has specific use cases
- CSS selectors and XPath are the most powerful locators
- Always prefer stable locators over fragile ones
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

def demonstrate_id_locator(driver):
    """Demonstrate ID locator strategy"""
    print("\n=== ID Locator Strategy ===")
    
    try:
        # Navigate to Google
        driver.get("https://www.google.com")
        wait = WebDriverWait(driver, 10)
        
        # Find search box by ID
        search_box = wait.until(EC.presence_of_element_located((By.ID, "APjFqb")))
        print("✓ Found search box using ID: 'APjFqb'")
        
        # Type in search box
        search_box.send_keys("Selenium automation testing")
        print("✓ Typed text in search box")
        
        # Find search button by ID
        search_button = driver.find_element(By.ID, "APjFqb")
        search_button.submit()
        print("✓ Submitted search form")
        
        time.sleep(3)
        
    except Exception as e:
        print(f"❌ ID locator failed: {e}")

def demonstrate_name_locator(driver):
    """Demonstrate Name locator strategy"""
    print("\n=== Name Locator Strategy ===")
    
    try:
        # Navigate to Facebook login
        driver.get("https://www.facebook.com")
        wait = WebDriverWait(driver, 10)
        
        # Find email field by name
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        print("✓ Found email field using NAME: 'email'")
        
        # Find password field by name
        password_field = driver.find_element(By.NAME, "pass")
        print("✓ Found password field using NAME: 'pass'")
        
        # Type in fields
        email_field.send_keys("test@example.com")
        password_field.send_keys("testpassword")
        print("✓ Typed in both fields")
        
        time.sleep(2)
        
    except Exception as e:
        print(f"❌ Name locator failed: {e}")

def demonstrate_class_name_locator(driver):
    """Demonstrate Class Name locator strategy"""
    print("\n=== Class Name Locator Strategy ===")
    
    try:
        # Navigate to Amazon
        driver.get("https://www.amazon.com")
        wait = WebDriverWait(driver, 10)
        
        # Find search box by class name
        search_box = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "nav-input")))
        print("✓ Found search box using CLASS_NAME: 'nav-input'")
        
        # Type in search box
        search_box.send_keys("laptop")
        print("✓ Typed 'laptop' in search box")
        
        time.sleep(2)
        
    except Exception as e:
        print(f"❌ Class name locator failed: {e}")

def demonstrate_tag_name_locator(driver):
    """Demonstrate Tag Name locator strategy"""
    print("\n=== Tag Name Locator Strategy ===")
    
    try:
        # Navigate to a simple page
        driver.get("https://www.google.com")
        wait = WebDriverWait(driver, 10)
        
        # Find all input elements
        input_elements = driver.find_elements(By.TAG_NAME, "input")
        print(f"✓ Found {len(input_elements)} input elements using TAG_NAME: 'input'")
        
        # Find all links
        link_elements = driver.find_elements(By.TAG_NAME, "a")
        print(f"✓ Found {len(link_elements)} link elements using TAG_NAME: 'a'")
        
        # Find all images
        image_elements = driver.find_elements(By.TAG_NAME, "img")
        print(f"✓ Found {len(image_elements)} image elements using TAG_NAME: 'img'")
        
    except Exception as e:
        print(f"❌ Tag name locator failed: {e}")

def demonstrate_link_text_locator(driver):
    """Demonstrate Link Text locator strategy"""
    print("\n=== Link Text Locator Strategy ===")
    
    try:
        # Navigate to Google
        driver.get("https://www.google.com")
        wait = WebDriverWait(driver, 10)
        
        # Find link by exact text
        gmail_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Gmail")))
        print("✓ Found Gmail link using LINK_TEXT: 'Gmail'")
        
        # Find link by partial text
        partial_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Gmail")
        print("✓ Found Gmail link using PARTIAL_LINK_TEXT: 'Gmail'")
        
        # Click on the link
        gmail_link.click()
        print("✓ Clicked on Gmail link")
        
        time.sleep(3)
        
    except Exception as e:
        print(f"❌ Link text locator failed: {e}")

def demonstrate_css_selector_locator(driver):
    """Demonstrate CSS Selector locator strategy"""
    print("\n=== CSS Selector Locator Strategy ===")
    
    try:
        # Navigate to Facebook
        driver.get("https://www.facebook.com")
        wait = WebDriverWait(driver, 10)
        
        # Find elements using CSS selectors
        email_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='email']")))
        print("✓ Found email field using CSS_SELECTOR: 'input[name=\"email\"]'")
        
        password_field = driver.find_element(By.CSS_SELECTOR, "input[name='pass']")
        print("✓ Found password field using CSS_SELECTOR: 'input[name=\"pass\"]'")
        
        # Find button using CSS selector
        login_button = driver.find_element(By.CSS_SELECTOR, "button[name='login']")
        print("✓ Found login button using CSS_SELECTOR: 'button[name=\"login\"]'")
        
        # Type in fields
        email_field.send_keys("test@example.com")
        password_field.send_keys("testpassword")
        print("✓ Typed in both fields")
        
        time.sleep(2)
        
    except Exception as e:
        print(f"❌ CSS selector locator failed: {e}")

def demonstrate_xpath_locator(driver):
    """Demonstrate XPath locator strategy"""
    print("\n=== XPath Locator Strategy ===")
    
    try:
        # Navigate to Amazon
        driver.get("https://www.amazon.com")
        wait = WebDriverWait(driver, 10)
        
        # Find search box using XPath
        search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='twotabsearchtextbox']")))
        print("✓ Found search box using XPATH: '//input[@id=\"twotabsearchtextbox\"]'")
        
        # Find search button using XPath
        search_button = driver.find_element(By.XPATH, "//input[@value='Go']")
        print("✓ Found search button using XPATH: '//input[@value=\"Go\"]'")
        
        # Type in search box
        search_box.send_keys("smartphone")
        print("✓ Typed 'smartphone' in search box")
        
        time.sleep(2)
        
    except Exception as e:
        print(f"❌ XPath locator failed: {e}")

def demonstrate_advanced_xpath(driver):
    """Demonstrate advanced XPath strategies"""
    print("\n=== Advanced XPath Strategies ===")
    
    try:
        # Navigate to Google
        driver.get("https://www.google.com")
        wait = WebDriverWait(driver, 10)
        
        # XPath with contains function
        search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@class, 'gLFyf')]")))
        print("✓ Found search box using XPATH with contains: '//input[contains(@class, \"gLFyf\")]'")
        
        # XPath with text function
        gmail_link = driver.find_element(By.XPATH, "//a[text()='Gmail']")
        print("✓ Found Gmail link using XPATH with text: '//a[text()=\"Gmail\"]'")
        
        # XPath with parent-child relationship
        search_form = driver.find_element(By.XPATH, "//form[@role='search']//input")
        print("✓ Found search input using XPATH with parent-child: '//form[@role=\"search\"]//input'")
        
        # XPath with position
        first_link = driver.find_element(By.XPATH, "(//a)[1]")
        print("✓ Found first link using XPATH with position: '(//a)[1]'")
        
    except Exception as e:
        print(f"❌ Advanced XPath failed: {e}")

def demonstrate_relative_vs_absolute_xpath(driver):
    """Demonstrate relative vs absolute XPath"""
    print("\n=== Relative vs Absolute XPath ===")
    
    try:
        # Navigate to a page
        driver.get("https://www.google.com")
        wait = WebDriverWait(driver, 10)
        
        # Absolute XPath (starts from root)
        absolute_xpath = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
        try:
            search_box_absolute = driver.find_element(By.XPATH, absolute_xpath)
            print("✓ Found element using absolute XPath")
        except:
            print("❌ Absolute XPath failed (too fragile)")
        
        # Relative XPath (more flexible)
        relative_xpath = "//input[@name='q']"
        search_box_relative = driver.find_element(By.XPATH, relative_xpath)
        print("✓ Found element using relative XPath: '//input[@name=\"q\"]'")
        
        # Relative XPath with contains
        flexible_xpath = "//input[contains(@class, 'gLFyf')]"
        search_box_flexible = driver.find_element(By.XPATH, flexible_xpath)
        print("✓ Found element using flexible XPath: '//input[contains(@class, \"gLFyf\")]'")
        
    except Exception as e:
        print(f"❌ XPath comparison failed: {e}")

def main():
    """Main function to demonstrate all locator strategies"""
    print("=== Selenium Element Location Strategies Tutorial ===\n")
    
    try:
        driver = setup_driver()
        print("✓ WebDriver setup successful!")
        
        # Demonstrate all locator strategies
        demonstrate_id_locator(driver)
        demonstrate_name_locator(driver)
        demonstrate_class_name_locator(driver)
        demonstrate_tag_name_locator(driver)
        demonstrate_link_text_locator(driver)
        demonstrate_css_selector_locator(driver)
        demonstrate_xpath_locator(driver)
        demonstrate_advanced_xpath(driver)
        demonstrate_relative_vs_absolute_xpath(driver)
        
        print("\n" + "="*60)
        print("✓ All locator strategies demonstrated successfully!")
        print("\nKey Takeaways:")
        print("- ID locators are fastest but not always available")
        print("- CSS selectors are faster than XPath")
        print("- XPath is most powerful but slower")
        print("- Always prefer stable locators over fragile ones")
        print("- Use relative XPath instead of absolute XPath")
        
    except Exception as e:
        print(f"❌ Tutorial failed: {e}")
    
    finally:
        if 'driver' in locals():
            print("\nClosing browser...")
            driver.quit()

if __name__ == "__main__":
    main()
