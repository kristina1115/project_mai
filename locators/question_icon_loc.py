from selenium.webdriver.common.by import By


TABS_NAME = (By.XPATH, "//div[contains(@class, 'Navigation__item')]/span")
TABS = (By.XPATH, "//div[contains(@class, 'Navigation__item')]")

ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'active')]/span")
TAB_2 = (By.XPATH, "//span[text()='Отчет']")
TAB_3 = (By.XPATH, "//span[text()='Настройки']")

ICON = (By.XPATH, "//div[contains(@class,'Header_Question')]")
HELP_TEXT = (By.XPATH, "//div[contains(@class,'UserOnboarding_Item')]")
PAGINATION_ELEMS = (By.XPATH, "//div[contains(@class, 'StepDot')]")
BUTTON_REPORT = (By.XPATH, "//button[text()='Аудитории']")
BUTTON_SETTINGS = (By.XPATH, "//button[text()='Тематики']")
TITLE_PAGE = (By.XPATH, "//span[text()= 'Картина дня за ']")

SUB_TABS = (By.XPATH, "//div[contains(@class, 'Switch_')]/button")
BUTTON = (By.XPATH, "//button[text()='Тематики']")

DATA = (By.XPATH,"//*[@data-onboarding]")
HINT_MODE = (By.XPATH, "//div[contains(@class, 'Onboarding_Backdrop')]")
