from pyautogui_start import company_sel, start_date_sel, end_date_sel, last_check, date_range, will_work
from selenuim_start import selenuim_start_f
from busfine_login import bus_fine_login_f
from busfine_driver_score_download import busfine_driver_score_download_f
from busfine_driver_score_erp_merge import busfine_driver_score_erp_merge_f


work_sel = will_work()
if work_sel =="운전자 일자별 탑승현황 다운로드":
    user_company_sel = company_sel()
    user_start_date_sel = start_date_sel()
    user_end_date_sel = end_date_sel()
    user_last_check = last_check(user_company_sel, user_start_date_sel, user_end_date_sel)
    dates = date_range(user_start_date_sel, user_end_date_sel)
    driver = selenuim_start_f()
    user_login = bus_fine_login_f(driver, user_company_sel)
    download = busfine_driver_score_download_f(driver, user_start_date_sel, user_end_date_sel,user_company_sel)

elif work_sel =="운전자 일자별 탑승현황 ERP MERGE":
    user_company_sel = company_sel()
    user_start_date_sel = start_date_sel()
    user_end_date_sel = end_date_sel()
    user_last_check = last_check(user_company_sel, user_start_date_sel, user_end_date_sel)
    dates = date_range(user_start_date_sel, user_end_date_sel)
    marge = busfine_driver_score_erp_merge_f(user_company_sel, dates)