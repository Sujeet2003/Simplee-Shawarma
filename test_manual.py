from selenium import webdriver
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

# HOME PAGE TESTING
class TestHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.home_url = "http://127.0.0.1:8000/"
        self.is_valid = True
        try:
            response = requests.get(self.home_url)
            if response.status_code == 200:
                logger.info("Home page URL is accessible.")
                self.driver.get(self.home_url)
            else:
                logger.error(f"Failed to load HOME page! Status Code: {response.status_code}")
                self.is_valid = False
        except requests.exceptions.RequestException as e:
            logger.error(f"Error checking HOME page URL: {e}")
            self.is_valid = False

    def test_home_container_section(self):
        assert "Simplee Shawarma" in self.driver.title
        logger.info("Homepage loaded successfully.")
        time.sleep(3)

        # Scroll down to 'Know More' button
        know_more_button = self.driver.find_element(By.ID, "knowMoreBtn")
        ActionChains(self.driver).move_to_element(know_more_button).perform()
        time.sleep(1)

        # Click 'Know More' button
        know_more_button.click()
        time.sleep(2)
        assert "About Shawarma" in self.driver.page_source
        logger.info("'Know More' button working successfully.")
        self.driver.back()
        time.sleep(2)

    # Test to Footer Section
    def test_footer_section(self):
        try:
            # Scroll down to footer
            footer = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "footer")))
            ActionChains(self.driver).move_to_element(footer).perform()
            time.sleep(2)
            
            # Test Main Location URL
            try:
                main_location = footer.find_element(By.XPATH, "//footer//a[contains(@href, 'google.com/maps')]")
                main_location_url = main_location.get_attribute("href")
                response = requests.get(main_location_url)
                
                if response.status_code == 200:
                    logger.info("Main Location URL is working, visiting now...")
                    main_location.click()
                    time.sleep(2)
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
                time.sleep(2)
                if "contact-us" in self.driver.current_url:
                    logger.info("Enquiry Button is working properly")
                    self.driver.back()
                    time.sleep(2)
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
                        time.sleep(2)
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
                        time.sleep(2)
                        logger.info(f"Successfully navigated to {self.driver.current_url}")
                        self.driver.back()
                        time.sleep(2)
                    else:
                        logger.warning(f"Skipping social media link {index+1}: No href found")
                time.sleep(3)
                self.driver.quit()
            except Exception as e:
                logger.error(f"Error testing Social Media links: {e}")
            
            logger.info("All footer tests completed successfully.")
        except Exception as e:
            logger.error(f"An error occurred while testing the footer: {e}")



test_home_page = TestHomePage(driver)
if test_home_page.is_valid:
    test_home_page.test_home_container_section()
    test_home_page.test_footer_section()
    logger.info("Test has been done for the HOME Page")
else:
    logger.warning("Skipping tests as the home page is not accessible.")


# ABOUT PAGE TESTING
class TestAboutPage:
    def __init__(self, driver):
        self.driver = driver

    def test_about_buttons(self):
        pass

