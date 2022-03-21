import pandas as pd

def busfine_driver_score_erp_merge_f(company, dates):
    print(f"ING__{company}_{dates[0]}_{dates[-1]}_운전자_일자별_탑승현황_MERGE")
    read_erp_data = pd.read_csv(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\ERP_DRIVING_SCORE\{company}_{dates[0]}_{dates[-1]}_ERP_DRIVING_SCORE.csv", encoding="euc-kr")
    read_erp_data["AmPm"] = read_erp_data["AmPm"].str.replace("1.", "", regex=True)
    read_erp_data["AmPm"] = read_erp_data["AmPm"].str.replace("2.", "", regex=True)
    read_erp_data = read_erp_data[["일자", "노선명", "차량번호", "AmPm", "사번", "성명", "상태",]]
    read_erp_data.columns =["운행일", "노선명", "차량번호", "오전/오후", "사번", "성명", "상태",]

    del_erp_data_a = read_erp_data[read_erp_data.상태 !="징계"]
    del_erp_data_b = del_erp_data_a[del_erp_data_a.상태 !="년차"]
    del_erp_data_c = del_erp_data_b[del_erp_data_b.상태 !="면제"]
    del_erp_data_d = del_erp_data_c[del_erp_data_c.상태 !="백신"]
    del_erp_data_e = del_erp_data_d[del_erp_data_d.상태 !="공가"]
    del_erp_data_f = del_erp_data_e[del_erp_data_e.상태 !="경조"]
    
    read_busfine_data = pd.read_excel(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\BUSFINE_DRIVER_SCORE\ATFER\{company}_{dates[0]}_{dates[-1]}_BUSFINE_DRIVING_SCORE.xlsx")

    result = pd.merge(read_busfine_data, del_erp_data_f, on=["운행일", "차량번호", "오전/오후"], how="outer")
    result.dropna(subset=["업체명"], inplace=True)
    result.to_csv(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\BUSFINE_DRIVER_SCORE_ERP_MERGE\{company}_{dates[0]}_{dates[-1]}_BUSFINE_DRIVING_SCORE_ERP_MERGE.csv", encoding="euc-kr")
    print("ALL_COMPLETE")