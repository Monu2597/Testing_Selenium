"""
Lesson 6: Browser Navigation and Window Handling
===============================================

This lesson covers:
1. Browser navigation (back, forward, refresh)
2. Window and tab management
3. Browser window sizing and positioning
4. Cookie management
5. JavaScript execution
6. Browser capabilities and options

Key Concepts:
- Browser navigation affects the current page state
- Window handles are unique identifiers for browser windows/tabs
- Cookies can be managed programmatically
- JavaScript execution can interact with page elements
- Browser options affect automation behavior
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
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

def demonstrate_browser_navigation(driver):
    """Demonstrate browser navigation operations"""
    print("\n=== Browser Navigation Operations ===")
    
    try:
        # Start with Google
        driver.get("https://www.google.com")
        wait = WebDriverWait(driver, 10)
        print("✓ Navigated to Google")
        
        # Get initial page info
        initial_title = driver.title
        initial_url = driver.current_url
        print(f"✓ Initial page: {initial_title} at {initial_url}")
        
        # Navigate to Facebook
        driver.get("https://www.facebook.com")
        wait.until(EC.title_contains("Facebook"))
        print("✓ Navigated to Facebook")
        
        facebook_title = driver.title
        facebook_url = driver.current_url
        print(f"✓ Facebook page: {facebook_title} at {facebook_url}")
        
        # Navigate to Amazon
        driver.get("https://www.amazon.com")
        wait.until(EC.title_contains("Amazon"))
        print("✓ Navigated to Amazon")
        
        amazon_title = driver.title
        amazon_url = driver.current_url
        print(f"✓ Amazon page: {amazon_title} at {amazon_url}")
        
        # Go back to Facebook
        driver.back()
        wait.until(EC.title_contains("Facebook"))
        print("✓ Went back to Facebook")
        
        # Verify we're back on Facebook
        current_title = driver.title
        if "Facebook" in current_title:
            print("✓ Successfully returned to Facebook")
        
        # Go forward to Amazon
        driver.forward()
        wait.until(EC.title_contains("Amazon"))
        print("✓ Went forward to Amazon")
        
        # Verify we're on Amazon
        current_title = driver.title
        if "Amazon" in current_title:
            print("✓ Successfully went forward to Amazon")
        
        # Refresh the page
        driver.refresh()
        wait.until(EC.title_contains("Amazon"))
        print("✓ Refreshed Amazon page")
        
        # Go back to Google
        driver.get("https://www.google.com")
        wait.until(EC.title_contains("Google"))
        print("✓ Returned to Google")
        
    except Exception as e:
        print(f"❌ Browser navigation failed: {e}")

def demonstrate_window_tab_management(driver):
    """Demonstrate window and tab management"""
    print("\n=== Window and Tab Management ===")
    
    try:
        # Start with Google
        driver.get("https://www.google.com")
        wait = WebDriverWait(driver, 10)
        print("✓ Started on Google")
        
        # Get current window handle
        main_window = driver.current_window_handle
        print(f"✓ Main window handle: {main_window}")
        
        # Get all window handles
        all_handles = driver.window_handles
        print(f"✓ Total windows/tabs: {len(all_handles)}")
        
        # Open new tab using JavaScript
        driver.execute_script("window.open('https://www.facebook.com', '_blank');")
        print("✓ Opened new tab with Facebook")
        
        # Wait for new tab to open
        time.sleep(2)
        
        # Get updated window handles
        all_handles = driver.window_handles
        print(f"✓ Total windows/tabs after opening new tab: {len(all_handles)}")
        
        # Switch to new tab
        new_tab = [handle for handle in all_handles if handle != main_window][0]
        driver.switch_to.window(new_tab)
        print("✓ Switched to new tab")
        
        # Verify we're on Facebook
        wait.until(EC.title_contains("Facebook"))
        print("✓ Successfully switched to Facebook tab")
        
        # Open another tab with Amazon
        driver.execute_script("window.open('https://www.amazon.com', '_blank');")
        print("✓ Opened another tab with Amazon")
        
        time.sleep(2)
        
        # Get all handles again
        all_handles = driver.window_handles
        print(f"✓ Total windows/tabs: {len(all_handles)}")
        
        # Switch to Amazon tab
        amazon_tab = [handle for handle in all_handles if handle not in [main_window, new_tab]][0]
        driver.switch_to.window(amazon_tab)
        print("✓ Switched to Amazon tab")
        
        # Verify we're on Amazon
        wait.until(EC.title_contains("Amazon"))
        print("✓ Successfully switched to Amazon tab")
        
        # Close current tab
        driver.close()
        print("✓ Closed Amazon tab")
        
        # Switch back to Facebook tab
        driver.switch_to.window(new_tab)
        print("✓ Switched back to Facebook tab")
        
        # Close Facebook tab
        driver.close()
        print("✓ Closed Facebook tab")
        
        # Switch back to main window
        driver.switch_to.window(main_window)
        print("✓ Switched back to main window")
        
        # Verify we're back on Google
        if "Google" in driver.title:
            print("✓ Successfully returned to Google main window")
        
    except Exception as e:
        print(f"❌ Window/tab management failed: {e}")

def demonstrate_window_sizing_positioning(driver):
    """Demonstrate window sizing and positioning"""
    print("\n=== Window Sizing and Positioning ===")
    
    try:
        # Navigate to a page
        driver.get("https://www.google.com")
        wait = WebDriverWait(driver, 10)
        print("✓ Navigated to Google")
        
        # Get current window size
        current_size = driver.get_window_size()
        print(f"✓ Current window size: {current_size['width']}x{current_size['height']}")
        
        # Get current window position
        current_position = driver.get_window_position()
        print(f"✓ Current window position: ({current_position['x']}, {current_position['y']})")
        
        # Set window size
        driver.set_window_size(800, 600)
        print("✓ Set window size to 800x600")
        
        # Verify new size
        new_size = driver.get_window_size()
        print(f"✓ New window size: {new_size['width']}x{new_size['height']}")
        
        # Set window position
        driver.set_window_position(100, 100)
        print("✓ Set window position to (100, 100)")
        
        # Verify new position
        new_position = driver.get_window_position()
        print(f"✓ New window position: ({new_position['x']}, {new_position['y']})")
        
        # Maximize window
        driver.maximize_window()
        print("✓ Maximized window")
        
        # Verify maximized size
        maximized_size = driver.get_window_size()
        print(f"✓ Maximized window size: {maximized_size['width']}x{maximized_size['height']}")
        
        # Minimize window
        driver.minimize_window()
        print("✓ Minimized window")
        
        time.sleep(2)
        
        # Maximize again
        driver.maximize_window()
        print("✓ Maximized window again")
        
        # Fullscreen mode
        driver.fullscreen_window()
        print("✓ Entered fullscreen mode")
        
        time.sleep(2)
        
        # Exit fullscreen
        driver.maximize_window()
        print("✓ Exited fullscreen mode")
        
    except Exception as e:
        print(f"❌ Window sizing/positioning failed: {e}")

def demonstrate_cookie_management(driver):
    """Demonstrate cookie management"""
    print("\n=== Cookie Management ===")
    
    try:
        # Navigate to a page
        driver.get("https://www.google.com")
        wait = WebDriverWait(driver, 10)
        print("✓ Navigated to Google")
        
        # Get all cookies
        cookies = driver.get_cookies()
        print(f"✓ Found {len(cookies)} cookies")
        
        # Display cookie information
        for i, cookie in enumerate(cookies[:3]):  # Show first 3 cookies
            print(f"  Cookie {i+1}: {cookie['name']} = {cookie['value']}")
            print(f"    Domain: {cookie.get('domain', 'N/A')}")
            print(f"    Path: {cookie.get('path', 'N/A')}")
            print(f"    Expiry: {cookie.get('expiry', 'N/A')}")
        
        # Add a custom cookie
        driver.add_cookie({
            'name': 'selenium_test_cookie',
            'value': 'test_value_123',
            'domain': '.google.com'
        })
        print("✓ Added custom cookie")
        
        # Verify cookie was added
        custom_cookie = driver.get_cookie('selenium_test_cookie')
        if custom_cookie:
            print(f"✓ Custom cookie found: {custom_cookie['value']}")
        
        # Delete specific cookie
        driver.delete_cookie('selenium_test_cookie')
        print("✓ Deleted custom cookie")
        
        # Verify cookie was deleted
        deleted_cookie = driver.get_cookie('selenium_test_cookie')
        if not deleted_cookie:
            print("✓ Custom cookie successfully deleted")
        
        # Delete all cookies
        driver.delete_all_cookies()
        print("✓ Deleted all cookies")
        
        # Verify all cookies deleted
        remaining_cookies = driver.get_cookies()
        print(f"✓ Remaining cookies: {len(remaining_cookies)}")
        
        # Refresh page to see effect
        driver.refresh()
        print("✓ Refreshed page after clearing cookies")
        
    except Exception as e:
        print(f"❌ Cookie management failed: {e}")

def demonstrate_javascript_execution(driver):
    """Demonstrate JavaScript execution"""
    print("\n=== JavaScript Execution ===")
    
    try:
        # Navigate to a page
        driver.get("https://www.google.com")
        wait = WebDriverWait(driver, 10)
        print("✓ Navigated to Google")
        
        # Execute JavaScript to get page title
        page_title = driver.execute_script("return document.title;")
        print(f"✓ Page title via JavaScript: {page_title}")
        
        # Execute JavaScript to get page URL
        page_url = driver.execute_script("return window.location.href;")
        print(f"✓ Page URL via JavaScript: {page_url}")
        
        # Execute JavaScript to get page height
        page_height = driver.execute_script("return document.body.scrollHeight;")
        print(f"✓ Page height via JavaScript: {page_height}")
        
        # Execute JavaScript to scroll down
        driver.execute_script("window.scrollTo(0, 500);")
        print("✓ Scrolled down 500 pixels via JavaScript")
        
        time.sleep(2)
        
        # Execute JavaScript to scroll to top
        driver.execute_script("window.scrollTo(0, 0);")
        print("✓ Scrolled to top via JavaScript")
        
        # Execute JavaScript to change page title
        driver.execute_script("document.title = 'Modified by Selenium';")
        print("✓ Changed page title via JavaScript")
        
        # Verify title change
        new_title = driver.title
        print(f"✓ New page title: {new_title}")
        
        # Execute JavaScript to highlight search box
        search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        driver.execute_script("arguments[0].style.border = '3px solid red';", search_box)
        print("✓ Highlighted search box via JavaScript")
        
        time.sleep(2)
        
        # Remove highlight
        driver.execute_script("arguments[0].style.border = '';", search_box)
        print("✓ Removed highlight via JavaScript")
        
        # Execute JavaScript to get element properties
        element_info = driver.execute_script("""
            var element = arguments[0];
            return {
                tagName: element.tagName,
                className: element.className,
                id: element.id,
                type: element.type
            };
        """, search_box)
        
        print(f"✓ Element info via JavaScript: {element_info}")
        
    except Exception as e:
        print(f"❌ JavaScript execution failed: {e}")

def demonstrate_browser_capabilities(driver):
    """Demonstrate browser capabilities and options"""
    print("\n=== Browser Capabilities and Options ===")
    
    try:
        # Get browser capabilities
        capabilities = driver.capabilities
        print("✓ Browser capabilities:")
        print(f"  Browser name: {capabilities.get('browserName', 'N/A')}")
        print(f"  Browser version: {capabilities.get('browserVersion', 'N/A')}")
        print(f"  Platform: {capabilities.get('platformName', 'N/A')}")
        print(f"  Accept insecure TLS: {capabilities.get('acceptInsecureCerts', 'N/A')}")
        
        # Get current page source length
        page_source = driver.page_source
        print(f"✓ Page source length: {len(page_source)} characters")
        
        # Get current page title
        page_title = driver.title
        print(f"✓ Page title: {page_title}")
        
        # Get current URL
        current_url = driver.current_url
        print(f"✓ Current URL: {current_url}")
        
        # Get page source (first 200 characters)
        page_source_preview = driver.page_source[:200]
        print(f"✓ Page source preview: {page_source_preview}...")
        
        # Get window handles
        window_handles = driver.window_handles
        print(f"✓ Number of window handles: {len(window_handles)}")
        
        # Get current window handle
        current_handle = driver.current_window_handle
        print(f"✓ Current window handle: {current_handle}")
        
        # Get window size
        window_size = driver.get_window_size()
        print(f"✓ Window size: {window_size}")
        
        # Get window position
        window_position = driver.get_window_position()
        print(f"✓ Window position: {window_position}")
        
        # Get cookies count
        cookies = driver.get_cookies()
        print(f"✓ Number of cookies: {len(cookies)}")
        
        # Get logs (if available)
        try:
            logs = driver.get_log('browser')
            print(f"✓ Browser logs count: {len(logs)}")
        except:
            print("✓ Browser logs not available")
        
    except Exception as e:
        print(f"❌ Browser capabilities failed: {e}")

def demonstrate_advanced_navigation(driver):
    """Demonstrate advanced navigation techniques"""
    print("\n=== Advanced Navigation Techniques ===")
    
    try:
        # Navigate to a page
        driver.get("https://www.google.com")
        wait = WebDriverWait(driver, 10)
        print("✓ Started on Google")
        
        # Navigate to a specific URL with parameters
        search_url = "https://www.google.com/search?q=selenium+automation+testing"
        driver.get(search_url)
        wait.until(EC.title_contains("selenium automation testing"))
        print("✓ Navigated to search results page")
        
        # Verify URL contains search query
        current_url = driver.current_url
        if "selenium+automation+testing" in current_url:
            print("✓ Search query found in URL")
        
        # Navigate to a different domain
        driver.get("https://www.selenium.dev")
        wait.until(EC.title_contains("Selenium"))
        print("✓ Navigated to Selenium official site")
        
        # Go back to Google
        driver.back()
        wait.until(EC.title_contains("Google"))
        print("✓ Went back to Google")
        
        # Navigate to a page that might redirect
        driver.get("https://httpbin.org/redirect/2")
        print("✓ Navigated to redirect page")
        
        time.sleep(3)
        
        # Check if we were redirected
        final_url = driver.current_url
        if "httpbin.org" in final_url:
            print(f"✓ Successfully handled redirect to: {final_url}")
        
        # Navigate to a page with authentication (will show login prompt)
        driver.get("https://httpbin.org/basic-auth/user/passwd")
        print("✓ Navigated to authentication page")
        
        time.sleep(2)
        
        # Return to Google
        driver.get("https://www.google.com")
        wait.until(EC.title_contains("Google"))
        print("✓ Returned to Google")
        
    except Exception as e:
        print(f"❌ Advanced navigation failed: {e}")

def main():
    """Main function to demonstrate all browser navigation and window handling"""
    print("=== Selenium Browser Navigation and Window Handling Tutorial ===\n")
    
    try:
        driver = setup_driver()
        print("✓ WebDriver setup successful!")
        
        # Demonstrate all navigation and window handling techniques
        demonstrate_browser_navigation(driver)
        demonstrate_window_tab_management(driver)
        demonstrate_window_sizing_positioning(driver)
        demonstrate_cookie_management(driver)
        demonstrate_javascript_execution(driver)
        demonstrate_browser_capabilities(driver)
        demonstrate_advanced_navigation(driver)
        
        print("\n" + "="*60)
        print("✓ All browser navigation and window handling demonstrated successfully!")
        print("\nKey Takeaways:")
        print("- Browser navigation affects page state and history")
        print("- Window handles are unique identifiers for windows/tabs")
        print("- JavaScript execution can interact with page elements")
        print("- Cookies can be managed programmatically")
        print("- Window sizing and positioning can be controlled")
        print("- Multiple tabs can be managed simultaneously")
        print("- Browser capabilities provide system information")
        
    except Exception as e:
        print(f"❌ Tutorial failed: {e}")
    
    finally:
        if 'driver' in locals():
            print("\nClosing browser...")
            driver.quit()

if __name__ == "__main__":
    main()
