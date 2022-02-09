from selenium import webdriver

def selenuim_start_f():
    driver = r"\\kjnas\KJNAS\1.기획부\9.개발팀\chromedriver"
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
    "download.default_directory": r"\\kjnas\KJNAS\1.기획부\9.개발팀\BUSFINE_DRIVER_SCORE\BEFORE",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,})
    driver = webdriver.Chrome(driver, chrome_options=options)
    return driver