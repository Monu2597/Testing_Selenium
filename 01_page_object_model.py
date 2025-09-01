"""
Lesson 7: Page Object Model (POM) Design Pattern
================================================

This lesson covers:
1. Page Object Model concept and benefits
2. Base page class implementation
3. Page classes for different websites
4. Test classes using POM
5. Best practices and patterns
6. Maintenance and scalability

Key Concepts:
- POM separates page logic from test logic
- Each page has its own class with locators and methods
- Base page class provides common functionality
- Tests become more readable and maintainable
- Locators are centralized and reusable
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

class BasePage:
    """Base page class with common functionality"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator):
        """Find element with explicit wait"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_elements(self, locator):
        """Find elements with explicit wait"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def click_element(self, locator):
        """Click element with explicit wait"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def type_text(self, locator, text):
        """Type text in element with explicit wait"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Get text from element"""
        element = self.find_element(locator)
        return element.text
    
    def is_element_visible(self, locator):
        """Check if element is visible"""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except:
            return False
    
    def wait_for_page_load(self):
        """Wait for page to load completely"""
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
    
    def get_page_title(self):
        """Get current page title"""
        return self.driver.title
    
    def get_current_url(self):
        """Get current URL"""
        return self.driver.current_url
    
    def take_screenshot(self, filename):
        """Take screenshot of current page"""
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        self.driver.save_screenshot(f"screenshots/{filename}.png")

class GooglePage(BasePage):
    """Google search page object"""
    
    # Locators
    SEARCH_BOX = (By.NAME, "q")
    SEARCH_BUTTON = (By.NAME, "btnK")
    SEARCH_RESULTS = (By.CSS_SELECTOR, "h3")
    GMAIL_LINK = (By.LINK_TEXT, "Gmail")
    IMAGES_LINK = (By.LINK_TEXT, "Images")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.google.com"
    
    def navigate_to(self):
        """Navigate to Google page"""
        self.driver.get(self.url)
        self.wait_for_page_load()
    
    def search(self, query):
        """Perform a search"""
        self.type_text(self.SEARCH_BOX, query)
        self.click_element(self.SEARCH_BUTTON)
        time.sleep(2)
    
    def get_search_results(self):
        """Get search result titles"""
        results = self.find_elements(self.SEARCH_RESULTS)
        return [result.text for result in results if result.text]
    
    def click_gmail(self):
        """Click on Gmail link"""
        self.click_element(self.GMAIL_LINK)
    
    def click_images(self):
        """Click on Images link"""
        self.click_element(self.IMAGES_LINK)
    
    def is_search_box_visible(self):
        """Check if search box is visible"""
        return self.is_element_visible(self.SEARCH_BOX)

class FacebookPage(BasePage):
    """Facebook login page object"""
    
    # Locators
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "pass")
    LOGIN_BUTTON = (By.NAME, "login")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgotten password?")
    CREATE_ACCOUNT_LINK = (By.LINK_TEXT, "Create new account")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.facebook.com"
    
    def navigate_to(self):
        """Navigate to Facebook page"""
        self.driver.get(self.url)
        self.wait_for_page_load()
    
    def enter_email(self, email):
        """Enter email address"""
        self.type_text(self.EMAIL_FIELD, email)
    
    def enter_password(self, password):
        """Enter password"""
        self.type_text(self.PASSWORD_FIELD, password)
    
    def click_login(self):
        """Click login button"""
        self.click_element(self.LOGIN_BUTTON)
    
    def login(self, email, password):
        """Complete login process"""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
        time.sleep(2)
    
    def click_forgot_password(self):
        """Click forgot password link"""
        self.click_element(self.FORGOT_PASSWORD_LINK)
    
    def click_create_account(self):
        """Click create account link"""
        self.click_element(self.CREATE_ACCOUNT_LINK)
    
    def is_email_field_visible(self):
        """Check if email field is visible"""
        return self.is_element_visible(self.EMAIL_FIELD)

class AmazonPage(BasePage):
    """Amazon page object"""
    
    # Locators
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")
    SEARCH_RESULTS = (By.CSS_SELECTOR, "h2 a span")
    CART_BUTTON = (By.ID, "nav-cart")
    ACCOUNT_LINK = (By.ID, "nav-link-accountList")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.amazon.com"
    
    def navigate_to(self):
        """Navigate to Amazon page"""
        self.driver.get(self.url)
        self.wait_for_page_load()
    
    def search_product(self, product_name):
        """Search for a product"""
        self.type_text(self.SEARCH_BOX, product_name)
        self.click_element(self.SEARCH_BUTTON)
        time.sleep(2)
    
    def get_product_results(self):
        """Get product search results"""
        results = self.find_elements(self.SEARCH_RESULTS)
        return [result.text for result in results if result.text]
    
    def click_cart(self):
        """Click on cart button"""
        self.click_element(self.CART_BUTTON)
    
    def click_account(self):
        """Click on account link"""
        self.click_element(self.ACCOUNT_LINK)
    
    def is_search_box_visible(self):
        """Check if search box is visible"""
        return self.is_element_visible(self.SEARCH_BOX)

class TestBase:
    """Base test class with common setup and teardown"""
    
    def setup_method(self):
        """Setup method called before each test"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        
        chrome_service = ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        # Initialize page objects
        self.google_page = GooglePage(self.driver)
        self.facebook_page = FacebookPage(self.driver)
        self.amazon_page = AmazonPage(self.driver)
    
    def teardown_method(self):
        """Teardown method called after each test"""
        if hasattr(self, 'driver'):
            self.driver.quit()

class TestGoogleSearch(TestBase):
    """Test class for Google search functionality"""
    
    def test_google_search(self):
        """Test Google search functionality"""
        print("\n=== Testing Google Search ===")
        
        # Navigate to Google
        self.google_page.navigate_to()
        print("✓ Navigated to Google")
        
        # Verify search box is visible
        assert self.google_page.is_search_box_visible(), "Search box should be visible"
        print("✓ Search box is visible")
        
        # Perform search
        search_query = "Selenium automation testing"
        self.google_page.search(search_query)
        print(f"✓ Searched for: {search_query}")
        
        # Get search results
        results = self.google_page.get_search_results()
        print(f"✓ Found {len(results)} search results")
        
        # Verify search results contain search query
        assert len(results) > 0, "Should have search results"
        print("✓ Search results are displayed")
        
        # Take screenshot
        self.google_page.take_screenshot("google_search_results")
        print("✓ Screenshot taken")
        
        print("✓ Google search test passed!")

class TestFacebookLogin(TestBase):
    """Test class for Facebook login functionality"""
    
    def test_facebook_login_form(self):
        """Test Facebook login form elements"""
        print("\n=== Testing Facebook Login Form ===")
        
        # Navigate to Facebook
        self.facebook_page.navigate_to()
        print("✓ Navigated to Facebook")
        
        # Verify email field is visible
        assert self.facebook_page.is_email_field_visible(), "Email field should be visible"
        print("✓ Email field is visible")
        
        # Test form filling (without actual login)
        test_email = "test@example.com"
        test_password = "testpassword"
        
        self.facebook_page.enter_email(test_email)
        print(f"✓ Entered email: {test_email}")
        
        self.facebook_page.enter_password(test_password)
        print("✓ Entered password")
        
        # Verify form is filled
        email_value = self.driver.find_element(*self.facebook_page.EMAIL_FIELD).get_attribute("value")
        assert email_value == test_email, "Email should be entered correctly"
        print("✓ Form filling verified")
        
        # Take screenshot
        self.facebook_page.take_screenshot("facebook_login_form")
        print("✓ Screenshot taken")
        
        print("✓ Facebook login form test passed!")

class TestAmazonSearch(TestBase):
    """Test class for Amazon search functionality"""
    
    def test_amazon_product_search(self):
        """Test Amazon product search"""
        print("\n=== Testing Amazon Product Search ===")
        
        # Navigate to Amazon
        self.amazon_page.navigate_to()
        print("✓ Navigated to Amazon")
        
        # Verify search box is visible
        assert self.amazon_page.is_search_box_visible(), "Search box should be visible"
        print("✓ Search box is visible")
        
        # Search for a product
        product_name = "laptop"
        self.amazon_page.search_product(product_name)
        print(f"✓ Searched for: {product_name}")
        
        # Get search results
        results = self.amazon_page.get_product_results()
        print(f"✓ Found {len(results)} product results")
        
        # Verify search results
        assert len(results) > 0, "Should have product results"
        print("✓ Product search results are displayed")
        
        # Take screenshot
        self.amazon_page.take_screenshot("amazon_search_results")
        print("✓ Screenshot taken")
        
        print("✓ Amazon product search test passed!")

def demonstrate_pom_pattern():
    """Demonstrate Page Object Model pattern"""
    print("=== Page Object Model Pattern Demonstration ===\n")
    
    try:
        # Setup driver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        
        chrome_service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        print("✓ WebDriver setup successful!")
        
        # Initialize page objects
        google_page = GooglePage(driver)
        facebook_page = FacebookPage(driver)
        amazon_page = AmazonPage(driver)
        
        # Demonstrate Google functionality
        print("\n--- Google Page Object Demo ---")
        google_page.navigate_to()
        print("✓ Navigated to Google")
        
        google_page.search("Page Object Model Selenium")
        print("✓ Performed search using POM")
        
        results = google_page.get_search_results()
        print(f"✓ Retrieved {len(results)} search results using POM")
        
        # Demonstrate Facebook functionality
        print("\n--- Facebook Page Object Demo ---")
        facebook_page.navigate_to()
        print("✓ Navigated to Facebook")
        
        facebook_page.enter_email("demo@example.com")
        print("✓ Entered email using POM")
        
        # Demonstrate Amazon functionality
        print("\n--- Amazon Page Object Demo ---")
        amazon_page.navigate_to()
        print("✓ Navigated to Amazon")
        
        amazon_page.search_product("smartphone")
        print("✓ Searched for product using POM")
        
        # Take screenshots
        google_page.take_screenshot("pom_demo_google")
        facebook_page.take_screenshot("pom_demo_facebook")
        amazon_page.take_screenshot("pom_demo_amazon")
        print("✓ Screenshots taken for all pages")
        
        print("\n✓ POM pattern demonstration completed successfully!")
        
    except Exception as e:
        print(f"❌ POM demonstration failed: {e}")
    
    finally:
        if 'driver' in locals():
            print("\nClosing browser...")
            driver.quit()

def main():
    """Main function to demonstrate Page Object Model"""
    print("=== Selenium Page Object Model Tutorial ===\n")
    
    try:
        # Demonstrate POM pattern
        demonstrate_pom_pattern()
        
        print("\n" + "="*60)
        print("✓ Page Object Model tutorial completed!")
        print("\nKey Takeaways:")
        print("- POM separates page logic from test logic")
        print("- Each page has its own class with locators and methods")
        print("- Base page class provides common functionality")
        print("- Tests become more readable and maintainable")
        print("- Locators are centralized and reusable")
        print("- Screenshots and logging can be easily added")
        print("- Page objects can be extended for different scenarios")
        
        print("\nNext Steps:")
        print("1. Run the test classes to see POM in action")
        print("2. Extend page objects with more functionality")
        print("3. Add data-driven testing capabilities")
        print("4. Implement reporting and logging")
        
    except Exception as e:
        print(f"❌ Tutorial failed: {e}")

if __name__ == "__main__":
    main()
