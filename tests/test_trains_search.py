from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.trains_page import TrainsPage
from pages.trains_results import TrainResultPage
from utils.logger import get_logger
logger = get_logger(__name__)

logger.info("Opening MakeMyTrip")
logger.info("Searching trains from Delhi to Mumbai")


def test_train_search(driver):
    driver.set_window_size(1920, 1080)

    driver.get("https://www.makemytrip.com/")

    wait = WebDriverWait(driver, 15)
    try:
        close_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[@data-cy='closeModal']"))
        )
        close_btn.click()
    except:
        pass
    trains = TrainsPage(driver)
    trains.open_trains_tab()
    trains.select_from_city("Delhi")
    trains.enter_to_city("Mumbai")
    trains.date_pick()
    trains.class_pick()
    trains.click_search()
    trains.capture_search_screenshot()

    result_page = TrainResultPage(driver)
    result_page.validate_results_loaded()
    result_page.print_train_names()
    result_page.extract_train_details()
    result_page.select_first_train()










