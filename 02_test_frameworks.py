"""
Lesson 8: Test Frameworks and pytest Integration
===============================================

This lesson covers:
1. pytest framework basics
2. Test organization and structure
3. Fixtures and setup/teardown
4. Parameterized testing
5. Test reporting and HTML output
6. Parallel test execution
7. Test data management

Key Concepts:
- pytest is a powerful testing framework for Python
- Fixtures provide reusable setup and teardown logic
- Parameterized tests reduce code duplication
- HTML reports provide detailed test execution information
- Parallel execution improves test suite performance
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# Test data for parameterized tests
SEARCH_QUERIES = [
    "Selenium automation testing",
    "Python programming",
    "Web development",
    "Machine learning",
    "Data science"
]

PRODUCT_NAMES = [
    "laptop",
    "smartphone",
    "headphones",
    "camera",
    "tablet"
]

class TestGoogleSearch:
    """Test class for Google search functionality"""
    
    @pytest.fixture(scope="class")
    def driver(self):
        """Setup WebDriver for the entire test class"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        
        chrome_service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        yield driver
        
        driver.quit()
    
    @pytest.fixture(autouse=True)
    def setup_teardown(self, driver):
        """Setup and teardown for each test method"""
        # Setup: Navigate to Google
        driver.get("https://www.google.com")
        time.sleep(2)
        
        yield
        
        # Teardown: Clear cookies and go back to Google
        driver.delete_all_cookies()
        driver.get("https://www.google.com")
    
    def test_google_page_title(self, driver):
        """Test Google page title"""
        assert "Google" in driver.title, f"Expected 'Google' in title, got '{driver.title}'"
    
    def test_search_box_visible(self, driver):
        """Test if search box is visible"""
        search_box = driver.find_element(By.NAME, "q")
        assert search_box.is_displayed(), "Search box should be visible"
    
    def test_search_functionality(self, driver):
        """Test basic search functionality"""
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium testing")
        search_box.submit()
        
        # Wait for results
        wait = WebDriverWait(driver, 10)
        results = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3")))
        
        assert results.is_displayed(), "Search results should be displayed"
    
    @pytest.mark.parametrize("query", SEARCH_QUERIES)
    def test_multiple_search_queries(self, driver, query):
        """Test search with multiple queries"""
        search_box = driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys(query)
        search_box.submit()
        
        # Wait for results
        wait = WebDriverWait(driver, 10)
        results = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3")))
        
        assert results.is_displayed(), f"Search results should be displayed for query: {query}"
        
        # Verify query in results
        page_source = driver.page_source.lower()
        assert query.lower() in page_source, f"Query '{query}' should appear in search results"
    
    @pytest.mark.slow
    def test_gmail_link(self, driver):
        """Test Gmail link functionality (marked as slow)"""
        gmail_link = driver.find_element(By.LINK_TEXT, "Gmail")
        gmail_link.click()
        
        # Wait for Gmail page to load
        wait = WebDriverWait(driver, 10)
        wait.until(EC.title_contains("Gmail"))
        
        assert "Gmail" in driver.title, "Should navigate to Gmail page"

class TestFacebookLogin:
    """Test class for Facebook login functionality"""
    
    @pytest.fixture(scope="class")
    def driver(self):
        """Setup WebDriver for the entire test class"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        
        chrome_service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=chrome_service, options=chrome_service)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        yield driver
        
        driver.quit()
    
    @pytest.fixture(autouse=True)
    def setup_teardown(self, driver):
        """Setup and teardown for each test method"""
        # Setup: Navigate to Facebook
        driver.get("https://www.facebook.com")
        time.sleep(2)
        
        yield
        
        # Teardown: Clear cookies
        driver.delete_all_cookies()
    
    def test_facebook_page_title(self, driver):
        """Test Facebook page title"""
        assert "Facebook" in driver.title, f"Expected 'Facebook' in title, got '{driver.title}'"
    
    def test_login_form_elements(self, driver):
        """Test if login form elements are present"""
        email_field = driver.find_element(By.NAME, "email")
        password_field = driver.find_element(By.NAME, "pass")
        login_button = driver.find_element(By.NAME, "login")
        
        assert email_field.is_displayed(), "Email field should be visible"
        assert password_field.is_displayed(), "Password field should be visible"
        assert login_button.is_displayed(), "Login button should be visible"
    
    def test_form_filling(self, driver):
        """Test form filling functionality"""
        email_field = driver.find_element(By.NAME, "email")
        password_field = driver.find_element(By.NAME, "pass")
        
        test_email = "test@example.com"
        test_password = "testpassword"
        
        email_field.send_keys(test_email)
        password_field.send_keys(test_password)
        
        # Verify form is filled
        assert email_field.get_attribute("value") == test_email, "Email should be entered correctly"
        assert password_field.get_attribute("value") == test_password, "Password should be entered correctly"
    
    @pytest.mark.parametrize("email,password", [
        ("user1@example.com", "pass1"),
        ("user2@example.com", "pass2"),
        ("user3@example.com", "pass3")
    ])
    def test_multiple_login_attempts(self, driver, email, password):
        """Test login with multiple credentials"""
        email_field = driver.find_element(By.NAME, "email")
        password_field = driver.find_element(By.NAME, "pass")
        
        email_field.clear()
        password_field.clear()
        
        email_field.send_keys(email)
        password_field.send_keys(password)
        
        # Verify form is filled
        assert email_field.get_attribute("value") == email, f"Email should be entered correctly: {email}"
        assert password_field.get_attribute("value") == password, f"Password should be entered correctly: {password}"

class TestAmazonSearch:
    """Test class for Amazon search functionality"""
    
    @pytest.fixture(scope="class")
    def driver(self):
        """Setup WebDriver for the entire test class"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        
        chrome_service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        yield driver
        
        driver.quit()
    
    @pytest.fixture(autouse=True)
    def setup_teardown(self, driver):
        """Setup and teardown for each test method"""
        # Setup: Navigate to Amazon
        driver.get("https://www.amazon.com")
        time.sleep(2)
        
        yield
        
        # Teardown: Clear cookies
        driver.delete_all_cookies()
    
    def test_amazon_page_title(self, driver):
        """Test Amazon page title"""
        assert "Amazon" in driver.title, f"Expected 'Amazon' in title, got '{driver.title}'"
    
    def test_search_box_visible(self, driver):
        """Test if search box is visible"""
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")
        assert search_box.is_displayed(), "Search box should be visible"
    
    @pytest.mark.parametrize("product", PRODUCT_NAMES)
    def test_product_search(self, driver, product):
        """Test product search functionality"""
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.clear()
        search_box.send_keys(product)
        
        search_button = driver.find_element(By.ID, "nav-search-submit-button")
        search_button.click()
        
        # Wait for results
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h2 a span")))
        
        # Verify search results
        results = driver.find_elements(By.CSS_SELECTOR, "h2 a span")
        assert len(results) > 0, f"Should have search results for product: {product}"

# Custom pytest markers
pytest_plugins = []

def pytest_configure(config):
    """Configure custom pytest markers"""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )

# Fixtures for cross-class usage
@pytest.fixture(scope="session")
def browser_driver():
    """Session-scoped WebDriver for cross-class tests"""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    chrome_service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    yield driver
    
    driver.quit()

@pytest.fixture
def wait(driver):
    """WebDriverWait fixture"""
    return WebDriverWait(driver, 10)

# Utility functions for tests
def take_screenshot(driver, test_name):
    """Take screenshot for test"""
    if not os.path.exists("test_screenshots"):
        os.makedirs("test_screenshots")
    
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"test_screenshots/{test_name}_{timestamp}.png"
    driver.save_screenshot(filename)
    return filename

def log_test_info(test_name, message):
    """Log test information"""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {test_name}: {message}")

# Test configuration
class TestConfig:
    """Test configuration class"""
    
    # Test timeouts
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 10
    PAGE_LOAD_TIMEOUT = 30
    
    # Test data
    BASE_URLS = {
        "google": "https://www.google.com",
        "facebook": "https://www.facebook.com",
        "amazon": "https://www.amazon.com"
    }
    
    # Screenshot settings
    TAKE_SCREENSHOTS = True
    SCREENSHOT_DIR = "test_screenshots"
    
    # Reporting settings
    GENERATE_HTML_REPORT = True
    REPORT_DIR = "test_reports"

# Example of a more complex test scenario
class TestCrossSiteNavigation:
    """Test class for cross-site navigation scenarios"""
    
    @pytest.fixture(scope="class")
    def driver(self):
        """Setup WebDriver for the entire test class"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        
        chrome_service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        yield driver
        
        driver.quit()
    
    def test_google_to_facebook_navigation(self, driver):
        """Test navigation from Google to Facebook"""
        # Start at Google
        driver.get("https://www.google.com")
        assert "Google" in driver.title, "Should start at Google"
        
        # Navigate to Facebook
        driver.get("https://www.facebook.com")
        assert "Facebook" in driver.title, "Should navigate to Facebook"
        
        # Go back to Google
        driver.back()
        assert "Google" in driver.title, "Should return to Google"
    
    def test_multiple_tabs_management(self, driver):
        """Test managing multiple tabs"""
        # Open Google in main tab
        driver.get("https://www.google.com")
        main_window = driver.current_window_handle
        
        # Open Facebook in new tab
        driver.execute_script("window.open('https://www.facebook.com', '_blank');")
        time.sleep(2)
        
        # Switch to new tab
        new_tab = [handle for handle in driver.window_handles if handle != main_window][0]
        driver.switch_to.window(new_tab)
        assert "Facebook" in driver.title, "Should be on Facebook tab"
        
        # Close new tab and return to main
        driver.close()
        driver.switch_to.window(main_window)
        assert "Google" in driver.title, "Should return to Google main tab"

# Test data management
class TestData:
    """Test data management class"""
    
    @staticmethod
    def get_search_queries():
        """Get search queries for testing"""
        return SEARCH_QUERIES
    
    @staticmethod
    def get_product_names():
        """Get product names for testing"""
        return PRODUCT_NAMES
    
    @staticmethod
    def get_test_credentials():
        """Get test credentials for testing"""
        return [
            {"email": "user1@example.com", "password": "pass1"},
            {"email": "user2@example.com", "password": "pass2"},
            {"email": "user3@example.com", "password": "pass3"}
        ]

if __name__ == "__main__":
    # Run tests with pytest
    print("=== Selenium Test Frameworks Tutorial ===\n")
    print("This file contains pytest test classes and fixtures.")
    print("To run the tests, use one of these commands:")
    print("\n1. Run all tests:")
    print("   pytest 03_advanced/02_test_frameworks.py -v")
    print("\n2. Run tests with HTML report:")
    print("   pytest 03_advanced/02_test_frameworks.py --html=test_reports/report.html --self-contained-html")
    print("\n3. Run only fast tests:")
    print("   pytest 03_advanced/02_test_frameworks.py -m 'not slow' -v")
    print("\n4. Run tests in parallel:")
    print("   pytest 03_advanced/02_test_frameworks.py -n auto -v")
    print("\n5. Run specific test class:")
    print("   pytest 03_advanced/02_test_frameworks.py::TestGoogleSearch -v")
    print("\n6. Run specific test method:")
    print("   pytest 03_advanced/02_test_frameworks.py::TestGoogleSearch::test_search_functionality -v")
