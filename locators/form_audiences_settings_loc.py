from selenium.webdriver.common.by import By


BUTTON_ADD = (By.XPATH, "//button[contains(text(), 'Добавить')]")
NAME_FIELD = (By.XPATH, "//input[@name='name']")
INDICATOR_FIELD = (By.XPATH, "//input[@name='indicators']")
INDICATORS_BLOCKS = (By.XPATH, "//div[contains(@class,'items')]//span")
INDICATOR_COLUMN = (By.XPATH, "//div[contains(@class, 'audiencesTable__row')]//span[text()]")

BUTTON_GREEN = (By.XPATH, "//button[contains(@class,'green')]")
BUTTON_RED = (By.XPATH, "//button[contains(@class,'red')]")
DELETE_BUTTON_GREEN = (By.XPATH, "//div[contains(@class,'positive')]/button")
NAME_INDICATOR_GREEN = (By.XPATH, "//div[contains(@class,'positive')]/span")
DELETE_BUTTON_RED = (By.XPATH, "//div[contains(@class,'negative')]/button")
NAME_INDICATOR_RED = (By.XPATH, "//div[contains(@class,'negative')]/span")

BUTTON_SUBMIT = (By.XPATH, "//button[@type='submit']")
BUTTON_CANCEL = (By.XPATH, "//button[text()= 'Отмена']")
TOPIC_ELEMENT = (By.XPATH, "//button[contains(@class, 'Position')]")

ORIENTATION = (By.XPATH, "//div[contains(@class, 'Orientation')]/span")

ROW_TOPIC = (By.XPATH, "//span/ancestor::div[contains(@class,'Row')]")
ROW_AUDIENCE = (By.XPATH, "//span/ancestor::div[contains(@class,'audiencesTable__row')]")

DELETE_CONFIRMATION_BUTTON = (By.XPATH, "//button[text()= 'Да']")

SEARCH_FIELD = (By.XPATH, "//input[@name='search']")
AUDIENCE_COLUMN = (By.XPATH, "//div[contains(@class,'ThematicsTable_Audience')]")
