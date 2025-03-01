from selenium_manual import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import logging, requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dataclasses import dataclass

# Setup logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Setup WebDriver
logger.info("Testing started using SELENIUM...")

driver_path = Service('chromedriver.exe')
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://127.0.0.1:8000/")

# navigate to the corresponding page
def navigate_and_validate(driver, xpath=None):
    """
    Navigates to the page associated with the given navigation item's XPath 
    and validates its response. If no XPath is provided, it validates the current page.
    
    driver: Selenium WebDriver instance
    xpath: XPath of the navigation menu item
    return: True if navigation is successful, False otherwise
    """
    time.sleep(3)  # Allow time for the page to load
    current_url = driver.current_url
    response = requests.get(current_url)
    
    if response.status_code != 200:
        logger.error(f"Invalid driver URL: {current_url}. Please make sure it's correct!")
        return False

    if xpath:
        try:
            nav_element = driver.find_element(By.XPATH, xpath)
            page_url = nav_element.get_attribute('href')

            if not page_url:
                logger.error("No valid URL found for the navigation item.")
                return False

            nav_element.click()
            time.sleep(3)  # Wait for the page to load

            response = requests.get(page_url)
            if response.status_code == 200:
                driver.get(page_url)
                logger.info(f"The {page_url} loaded successfully.")
                return True
            else:
                logger.error(f"OOPS, the {page_url} is not responding! Status Code: {response.status_code}")
                return False

        except Exception as e:
            logger.error(f"Error while navigating: {e}")
            return False

    logger.info(f"Current URL {current_url} is accessible.")
    return True


# HOME Page Test
class TestHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.is_valid = navigate_and_validate(driver)

    def test_home_container_section(self):
        assert "Simplee Shawarma" in self.driver.title
        logger.info("Homepage loaded successfully.")
        time.sleep(3)

        # Scroll down to 'Know More' button
        know_more_button = self.driver.find_element(By.ID, "knowMoreBtn")
        ActionChains(self.driver).move_to_element(know_more_button).perform()
        time.sleep(2)

        # Click 'Know More' button
        know_more_button.click()
        time.sleep(3)
        assert "About Shawarma" in self.driver.page_source
        logger.info("'Know More' button working successfully.")
        self.driver.back()
        time.sleep(3)

    # Test to Footer Section
    def test_footer_section(self):
        try:
            # Scroll down to footer
            footer = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "footer")))
            ActionChains(self.driver).move_to_element(footer).perform()
            time.sleep(3)
            
            # Test Main Location URL
            try:
                main_location = footer.find_element(By.XPATH, "//footer//a[contains(@href, 'google.com/maps')]")
                main_location_url = main_location.get_attribute("href")
                response = requests.get(main_location_url)
                
                if response.status_code == 200:
                    logger.info("Main Location URL is working, visiting now...")
                    main_location.click()
                    time.sleep(3)
                    self.driver.back()
                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "footer")))
                    logger.info("Returned to the main page successfully")
                else:
                    logger.info(f"Main Location URL not working: {response.status_code}")
            except Exception as e:
                logger.error(f"Error testing Main Location URL: {e}")
            
            # Test Enquiry Button
            try:
                enquiry_btn = footer.find_element(By.ID, "enquiryNow")
                enquiry_btn.click()
                time.sleep(3)
                if "contact-us" in self.driver.current_url:
                    logger.info("Enquiry Button is working properly")
                    self.driver.back()
                    time.sleep(3)
                else:
                    logger.error(f"Redirection failed! Current URL: {self.driver.current_url}")
            except Exception as e:
                logger.error(f"Error clicking the Enquiry Button: {e}")
            
            # Test Other Footer Links (Locations & Policies)
            try:
                others_links = footer.find_elements(By.CSS_SELECTOR, ".others a")
                for index, link in enumerate(others_links):
                    href = link.get_attribute("href")
                    text = link.text.strip()
                    if href:
                        logger.info(f"Testing link {index+1}: {text}")
                        link.click()
                        time.sleep(3)
                        logger.info(f"Successfully navigated to {self.driver.current_url}")
                        self.driver.back()
                        time.sleep(3)
                    else:
                        logger.warning(f"Skipping link {index+1}: No href attribute found")            
            except Exception as e:
                logger.error(f"Error testing OTHER footer links: {e}")
            
            # Test Social Media Links
            try:
                social_media_links = footer.find_elements(By.CSS_SELECTOR, ".social-media a")
                for index, link in enumerate(social_media_links):
                    href = link.get_attribute("href")
                    if href:
                        logger.info(f"Testing social media link {index+1}: {href}")
                        link.click()
                        time.sleep(3)
                        logger.info(f"Successfully navigated to {self.driver.current_url}")
                        self.driver.back()
                        time.sleep(3)
                    else:
                        logger.warning(f"Skipping social media link {index+1}: No href found")
                time.sleep(3)
            except Exception as e:
                logger.error(f"Error testing Social Media links: {e}")
            
            logger.info("All footer tests completed successfully.")
        except Exception as e:
            logger.error(f"An error occurred while testing the footer: {e}")


# ABOUT Page Test
class TestAboutPage:
    def __init__(self, driver):
        self.driver = driver
        self.is_valid = navigate_and_validate(driver, "//*[@id='navbarNav']/ul/li[2]/a")
    
    def test_functions(self):
        explore_menu_btn = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-custom.mt-3")
        explore_menu_btn.click()
        time.sleep(3)
        logger.info("Explore more button has been tested successfully from the about page")
        self.driver.back()
        time.sleep(3)


# MENU Page Test
class TestMenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.is_valid = navigate_and_validate(driver, "//*[@id='navbarNav']/ul/li[3]/a")
    
    def test_menu_items_display(self):
        logger.info("Testing menu items display...")
        items = self.driver.find_elements(By.CLASS_NAME, "item")
        assert len(items) > 0, "No menu items found on the page"
        
        first_item = items[0].find_element(By.CLASS_NAME, "item-name")
        assert first_item.is_displayed()
        assert first_item.text.strip() != "", "Item name is missing"
        logger.info("Menu items display test passed.")


# CONTACT Page Test
class TestContactPage:
    def __init__(self, driver):
        self.driver = driver
        self.is_valid = navigate_and_validate(driver, "//*[@id='navbarNav']/ul/li[4]/a")
    
    def check_contact_form(self):
        logger.info("Testing contact form submission...")
        try:
            name_field = self.driver.find_element(By.ID, "id_name")
            email_field = self.driver.find_element(By.ID, "id_email")
            subject_field = self.driver.find_element(By.ID, "id_subject")
            message_field = self.driver.find_element(By.ID, "id_message")
            submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

            name_field.send_keys("Name Test ")
            email_field.send_keys("test@gmail.com")
            subject_field.send_keys("Test Subject")
            message_field.send_keys("This is a test message.")

            submit_button.click()
            time.sleep(3)

            success_message = self.driver.find_element(By.ID, "success-message")
            assert success_message.is_displayed(), "Success message is not displayed!"
            logger.info("Contact form submission test passed.")
        except Exception as e:
            logger.error(f"Error while testing contact form: {e}")

# Home Page Test objects
test_home_page = TestHomePage(driver)
if test_home_page.is_valid:
    test_home_page.test_home_container_section()
    test_home_page.test_footer_section()
    logger.info("Test has been done for the HOME Page")
else:
    logger.warning("Skipping tests as the home page is not accessible.")

# About Page Test objects
test_about_page = TestAboutPage(driver)
if test_about_page.is_valid:
    test_about_page.test_functions()
    logger.info("Test has been done for the ABOUT Page successfully.")
else:
    logger.warning("Skipping tests as the about page is not accessible.")

# Menu Page Test objects
test_menu_page = TestMenuPage(driver)
if test_menu_page.is_valid:
    test_menu_page.test_menu_items_display()
    logger.info("Test has been done for the MENU Page successfully.")
else:
    logger.warning("Skipping tests as the menu page is not accessible.")

# Contact Page Test Objects
test_contact_page = TestContactPage(driver)
if test_contact_page.is_valid:
    test_contact_page.check_contact_form()
    logger.info("Test has been done for the CONTACT Page successfully.")
else:
    logger.warning("Skipping tests as the contact page is not accessible.")

driver.quit()