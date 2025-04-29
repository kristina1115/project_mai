from selenium.webdriver.common.by import By


NAME_FIELD = (By.XPATH, "//input[@name='name']")
SELECT_FIELD = (By.XPATH, "//input[contains(@class,'SelectField')]")
IDENTIFIER_FIELD = (By.XPATH, "//input[@name='address']")

# CHANNEL_TELEGRAM = (By.XPATH, "//div[text()='Telegram']")
# CHANNEL_INNER = (By.XPATH, "//div[text()='Внутренний']")
# CHANNELS = (By.XPATH, "//div[contains(@class,'itemsWrapper')]")

ROW = (By.XPATH, "//div[contains(@class, 'Name')]//span")
DELETE_BUTTON = (By.XPATH, "//div[contains(@class, 'Trash')]")

CHANNEL_TITLE_COLUMN = (By.XPATH, "//span[text()='Привязанные каналы']")
