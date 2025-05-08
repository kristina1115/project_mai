from selenium.webdriver.common.by import By


CLASS_SELECT = (By.XPATH, "//input[@placeholder='Выбор класса']")
# CLASS_OPTION_BUSINESS = (By.XPATH, "//div[@role='option']/span[text()='Бизнес']")
# CLASS_OPTION_OTHER = (By.XPATH, "//div[@role='option']/span[text()='Прочее']")
# CLASS_LIST_BOX = (By.XPATH, "//div[@role= 'listbox']")

CHANNELS_SELECT = (By.XPATH, "//div[contains(@class, 'values')]/input")
CHANNELS_OPTION = (By.XPATH, "//div[text()='МГТУ тестовый']")

PUBLICATION_CHANNELS = (By.XPATH, "//div[contains(@class, 'MultiSelect-values')]/input")
PUBLICATION_OPTION = (By.XPATH, "//div[contains(@class, 'Source')]/span[text()]")

CHANNEL_IN_TABLE = (By.XPATH, "//span[text()='Агрегатор. Москва']")

LANGUAGES_FIELD = (By.XPATH, "//button[contains(@class, 'LanguageInput')]")
ALL_LANGUAGES = (By.XPATH, "//label[text()= 'Все Языки']")
CHECKBOX_ALL_LANGUAGES = (By.XPATH, "//input[@id='language-all']")
LANGUAGE_NAME = (By.XPATH, "//div[contains(@class,'Language')]//span[text()]")

COUNTRY_FIELD = (By.XPATH, "//input[@placeholder='Выбор страны']")
REGION_OPTION = (By.XPATH, "//div[@role='option']")
REGION_FIELD = (By.XPATH, "//input[@placeholder='Выбор региона']")
GEOGRAPHY_BUTTON = (By.XPATH, "//button[contains(@class, 'Geography') and text()='Добавить']")
GEOGRAPHY = (By.XPATH, "//div[contains(@class, 'values')]//span")
GEOGRAPHY_IN_TABLE = (By.XPATH, "//a/following-sibling::span")

AI_BUTTON = (By.XPATH, "//button[@role='switch']")
AI_BUTTON_IN_TABLE = (By.XPATH, "//div[contains(@class,'Column_4')]//button")

KEYWORD_FIELD = (By.XPATH, "//input[@name='keywords']")
KEYWORD_BUTTON = (By.XPATH, "//div[contains(@class,'KeyWord')]/button")
KEYWORD = (By.XPATH, "//div[contains(@class,'ItemKey')]//span")

SOURCE_FIELD = (By.XPATH, "//input[contains(@class,'PublicationSource')]")
SOURCE_OPTION = (By.XPATH, "//span[text()='Добавить канал'] ")
LINK_FIELD = (By.XPATH, "//input[@name='channel-link'] ")
LINK_SUBMIT = (By.XPATH, "//div[contains(@class, 'TextField')]/following-sibling::button")
SOURCE_BUTTON = (By.XPATH, "//button[contains(@class, 'Source')]")

DELETE_MESSAGE1 = (By.XPATH, "//div[text()='Удаляем тематику']")
DELETE_MESSAGE2 = (By.XPATH, "//div[@role='status']")

SEARCH_TOPIC = (By.XPATH, "//input[@name='query']")
TOPIC_TITLE_COLUMN = (By.XPATH, "//span[text()='Класс событий']")
TOPIC_NAME = (By.XPATH, "//div[contains(@class, 'Table')]/a/span")
TOPIC_DELETE_BUTTON = (By.XPATH, "//div[contains(@class, 'PositionBox')]")
