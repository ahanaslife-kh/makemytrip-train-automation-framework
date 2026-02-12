from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger
logger = get_logger(__name__)
class TrainResultPage(BasePage):

    TRAINS_FOUND_TEXT = (
        By.XPATH,
        "//div[contains(text(),'trains found')]"
    )
    #TRAINS = (By.XPATH, "//div[@data-testid='listing-card']")
    TRAIN_NAMES = (By.XPATH, "//p[@data-testid='train-name']")
    TRAIN_PRICES = (By.XPATH, "//p[contains(@class,'Cards_totalText')]")
    FIRST_TRAIN_CARD = (By.XPATH, "(//div[@data-testid='listing-card'])[1]")
    TRAIN_DURATIONS = (
        By.XPATH,
        "//div[@data-testid='travel-time']"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def validate_results_loaded(self):
        element = self.wait_for(self.TRAINS_FOUND_TEXT)
        assert "trains found" in element.text.lower()
        logger.info(f"Results Loaded: {element.text}")

    def print_train_names(self):
        names = self.driver.find_elements(*self.TRAIN_NAMES)

        logger.info("First 5 Train Names:")
        for name in names[:5]:
            logger.info(name.text)

        assert len(names) > 0

    def validate_train_names(self):
        names = self.driver.find_elements(*self.TRAIN_NAMES)

        logger.info("\nValidating Train Names...")
        assert len(names) >= 5

        for name in names[:5]:
            logger.info(name.text)
            assert name.text.strip() != ""

    def extract_train_details(self):
        names = self.driver.find_elements(*self.TRAIN_NAMES)
        durations = self.driver.find_elements(*self.TRAIN_DURATIONS)
        prices = self.driver.find_elements(*self.TRAIN_PRICES)

        logger.info("\nTrain Details:")

        for i in range(min(2, len(names))):
            logger.info(
                f"Train: {names[i].text} | "
                f"Duration: {durations[i].text} | "
                f"Price: {prices[i].text}"
            )

        assert len(names) > 5

    def select_first_train(self):

            first_train = self.wait_for(self.FIRST_TRAIN_CARD)

            self.driver.execute_script("arguments[0].scrollIntoView(true);", first_train)
            self.driver.execute_script("arguments[0].click();", first_train)

            logger.info("First train selected successfully.")

    def capture_screenshot(self):
        self.driver.save_screenshot("train_results.png")
        logger.info("Screenshot captured successfully.")














