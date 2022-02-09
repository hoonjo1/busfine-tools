import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def bus_fine_login_f(driver, company):
    url = "https://busfine.gtrans.or.kr/"
    driver.get(url)

    if company == "경진여객":
        id = "경진여객"
        password = "busfine_kj_25!"
    elif company == "용남고속":
        id = "용남고속"
        password = "busfine_yn_27!"
    elif company == "제부여객":
        id = "제부여객"
        password = "ggbusfine_jb_21!"

    login_id = driver.find_element(By.ID, "id")
    pyperclip.copy(id)
    driver.implicitly_wait(10)
    login_id.send_keys(Keys.CONTROL, "v")

    login_pw = driver.find_element(By.ID, "password")
    pyperclip.copy(password)
    driver.implicitly_wait(10)
    login_pw.send_keys(Keys.CONTROL, "v")
    
    login_bth = driver.find_element(By.CLASS_NAME, "loginBtn")
    driver.implicitly_wait(10)
    login_bth.click()