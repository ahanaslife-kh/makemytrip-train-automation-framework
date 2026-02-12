import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class TrainsPage(BasePage):

    TRAINS_TAB = (By.XPATH, "//span[text()='Trains']")

    FROM_INPUT = (By.ID, "fromCity")
    TO_INPUT = (By.ID, "toCity")

    ACTIVE_INPUT = (By.XPATH, "//input[@placeholder='From' or @placeholder='To']")

    SEARCH_BUTTON = (By.XPATH, "//a[@data-cy='submit']")

    def open_trains_tab(self):
        self.click(self.TRAINS_TAB)

    def select_from_city(self, city):
        self.click(self.FROM_INPUT)
        self.type(self.ACTIVE_INPUT, city)
        self.driver.find_element(*self.ACTIVE_INPUT).send_keys(Keys.ARROW_DOWN)
        self.driver.find_element(*self.ACTIVE_INPUT).send_keys(Keys.ENTER)

        self.driver.find_element(By.TAG_NAME, "body").click()


    def enter_to_city(self, city):
        # 1️⃣ Click To label (activates autosuggest)
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "input[placeholder='To']")
        )).click()

        # 2️⃣ Wait for active autosuggest input
        to_input = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[placeholder='To']")
        ))

        to_input.clear()
        to_input.send_keys("Mumbai")
        # Wait for suggestions to load
        mumbai_option = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//li[@role='option']//span[contains(text(),'Mumbai')]")
        ))

        self.driver.execute_script("arguments[0].click();", mumbai_option)

    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException

    def close_popup_if_present(self):
        try:
            close_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//img[@alt='minimize']"))
            )
            close_btn.click()

            # Wait until popup disappears
            WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element_located((By.XPATH, "//img[@alt='minimize']"))
            )

        except:
            pass
        search_button = self.driver.find_element(By.XPATH, "//a[@data-cy='submit']")
        self.driver.execute_script("arguments[0].click();", search_button)
    def date_picker(self):
        departure = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@data-cy='departure']"))
        )
        departure.click()
        select_date = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='DayPicker-Day' and text()='12']"))
        )
        select_date.click()
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, "//div[contains(@class,'dayPicker')]"))
        )

    def class_Select(self):
            self.wait.until(
                EC.element_to_be_clickable((By.ID, "travelClass"))
            ).click()
            self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//li[@data-cy='SL']"))
            ).click()

    def click_search(self):
        # Close calendar if open
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(
                (By.XPATH, "//div[contains(@class,'rsw_widgetOpen')]")
            )
        )

        search_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@data-cy='submit']"))
        )

        self.driver.execute_script("arguments[0].click();", search_btn)
