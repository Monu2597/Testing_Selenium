"""
Lesson 1: WebDriver Setup and Configuration
==========================================

This lesson covers:
1. Setting up Chrome WebDriver
2. Setting up Firefox WebDriver
3. Basic browser operations
4. WebDriver manager for automatic driver updates

Key Concepts:
- WebDriver is the interface between Selenium and the browser
- webdriver-manager automatically downloads and manages browser drivers
- Different browsers have different WebDriver implementations
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

def setup_chrome_driver():
    """Setup Chrome WebDriver with options"""
    print("Setting up Chrome WebDriver...")
    
    # Chrome options for better automation
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--start-maximized")  # Start browser maximized
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Hide automation
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    # Setup Chrome service with automatic driver management
    chrome_service = ChromeService(ChromeDriverManager().install())
    
    # Create WebDriver instance
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    
    # Hide automation detection
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    return driver

def setup_firefox_driver():
    """Setup Firefox WebDriver with options"""
    print("Setting up Firefox WebDriver...")
    
    # Firefox options
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--start-maximized")
    
    # Setup Firefox service with automatic driver management
    firefox_service = FirefoxService(GeckoDriverManager().install())
    
    # Create WebDriver instance
    driver = webdriver.Firefox(service=firefox_service, options=firefox_options)
    
    return driver

def basic_browser_operations(driver):
    """Demonstrate basic browser operations"""
    print("\nPerforming basic browser operations...")
    
    # Navigate to a website
    print("1. Navigating to Google...")
    driver.get("https://www.google.com")
    time.sleep(2)
    
    # Get page title
    title = driver.title
    print(f"2. Page title: {title}")
    
    # Get current URL
    current_url = driver.current_url
    print(f"3. Current URL: {current_url}")
    
    # Get page source length
    page_source_length = len(driver.page_source)
    print(f"4. Page source length: {page_source_length} characters")
    
    # Browser window operations
    print("5. Browser window operations...")
    window_handle = driver.current_window_handle
    print(f"   Current window handle: {window_handle}")
    
    # Get window size
    window_size = driver.get_window_size()
    print(f"   Window size: {window_size}")
    
    # Get window position
    window_position = driver.get_window_position()
    print(f"   Window position: {window_position}")

def demonstrate_browser_controls(driver):
    """Demonstrate browser control operations"""
    print("\nDemonstrating browser controls...")
    
    # Navigate to different pages
    print("1. Navigating to different pages...")
    
    driver.get("https://www.google.com")
    time.sleep(1)
    print("   - Navigated to Google")
    
    driver.get("https://www.facebook.com")
    time.sleep(1)
    print("   - Navigated to Facebook")
    
    # Browser navigation
    print("2. Browser navigation...")
    
    driver.back()
    time.sleep(1)
    print("   - Went back to Google")
    
    driver.forward()
    time.sleep(1)
    print("   - Went forward to Facebook")
    
    driver.refresh()
    time.sleep(1)
    print("   - Refreshed Facebook page")

def main():
    """Main function to demonstrate WebDriver setup"""
    print("=== Selenium WebDriver Setup Tutorial ===\n")
    
    # Setup Chrome driver
    try:
        chrome_driver = setup_chrome_driver()
        print("✓ Chrome WebDriver setup successful!")
        
        # Demonstrate basic operations
        basic_browser_operations(chrome_driver)
        demonstrate_browser_controls(chrome_driver)
        
        # Clean up
        print("\nClosing Chrome browser...")
        chrome_driver.quit()
        
    except Exception as e:
        print(f"❌ Chrome setup failed: {e}")
    
    print("\n" + "="*50)
    
    # Setup Firefox driver (optional - uncomment if Firefox is installed)
    try:
        firefox_driver = setup_firefox_driver()
        print("✓ Firefox WebDriver setup successful!")
        
        # Demonstrate basic operations
        basic_browser_operations(firefox_driver)
        demonstrate_browser_controls(firefox_driver)
        
        # Clean up
        print("\nClosing Firefox browser...")
        firefox_driver.quit()
        
    except Exception as e:
        print(f"❌ Firefox setup failed: {e}")
        print("Note: Firefox setup is optional. Chrome setup is sufficient for learning.")

if __name__ == "__main__":
    main()
