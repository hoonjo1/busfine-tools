import os
import time
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains


def busfine_driver_score_download_f(driver, select_start_date, select_end_date, company):
    time.sleep(2)
    driver.get("https://busfine.gtrans.or.kr/calculate/quarter/GBFM3065.gbf")
    start_date = driver.find_element(By.ID, "sc_FROM_COLL_DATE")
    end_date = driver.find_element(By.ID, "sc_TO_COLL_DATE")
    
    start_date.click()
    pyperclip.copy(select_start_date)
    driver.implicitly_wait(10)
    start_date.send_keys(Keys.CONTROL, 'v') # windows
    # ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform() # mac

    end_date.click()
    pyperclip.copy(select_end_date)
    driver.implicitly_wait(10)
    end_date.send_keys(Keys.CONTROL, 'v') # windows
    # ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform() # mac

    inquire_bth = driver.find_element(By.CLASS_NAME, "btn.btn_gold.btn_down")
    driver.implicitly_wait(10)
    inquire_bth.click()
    driver.implicitly_wait(10)


    download_bth = driver.find_element(By.CLASS_NAME, "btn.btn_darkblue.btn_down")
    driver.implicitly_wait(10)
    download_bth.click()
    driver.implicitly_wait(10)
    
    try:
        approve = Alert(driver)
        approve.accept()
    except:
        pass
    
    time.sleep(15)
    file_name_check = r"\\kjnas\KJNAS\1.기획부\9.개발팀\BUSFINE_DRIVER_SCORE\BEFORE"
    file_name_list = os.listdir(file_name_check)

    for i in file_name_list:
        beforeFileName = rf"\\kjnas\KJNAS\1.기획부\9.개발팀\BUSFINE_DRIVER_SCORE\BEFORE\{i}"
        afterFileName = rf"\\kjnas\KJNAS\1.기획부\9.개발팀\BUSFINE_DRIVER_SCORE\ATFER\{company}_{select_start_date}_{select_end_date}_BUSFINE_DRIVING_SCORE.xlsx"
        os.rename(beforeFileName, afterFileName)
        print(f"_____Complete______",afterFileName)
        
    driver.quit()
