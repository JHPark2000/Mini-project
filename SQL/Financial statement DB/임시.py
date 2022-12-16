'''
conn = create_engine("oracle+cx_oracle://SYSTEM:521122@localhost:1521/?service_name=XE")
corp_info = pd.read_excel(r"C:\Users\parkj\Desktop\Git\Mini-project\SQL\Financial statement DB\corpcode.xlsx")
corp_info.to_sql('c_info',conn,if_exists='replace')

liquidity_ratio = ["총자산회전율","자기자본회전율","재고자산회전율","매출채권회전율"]
profit_ratio = ["매출순이익율","총자산순이익율","자기자본순이익율","매출영업이익률","이자보상비율"]
stable_ratio = ["자기자본비율","유동비율","당좌비율","비유동비율","현금및현금성자산비율"]
growth_ratio = ["총자산증가율","유형자산증가율","유동자산증가율","재고자산증가율","자기자본증가율","매출액증가율"]

while True:
    sprit_line = "====================================================================="
    
    print(sprit_line)
    print("2015년 이후 자료만 수집할 수 있습니다.")
    print(sprit_line)

    IN_CorpNAME = input("검색을 원하는 기업명을 입력하세요.")
    IN_START_Period = input("검색 시작 연도를 입력하세요. 종료를 원할시 0000을 입력하세요. 2015년 이후 자료만 수집 가능합니다.")
    print(sprit_line)
    IN_FINSH_Period = input("검색 종료 연도를 입력하세요. \n 입력값이 없으면 시작 연도 이후의 모든 재무제표를 수집합니다. \n 시작 연도와 동일하면 단일연도 자료를 수집합니다.")

    try:
        IN_START_Period = int(IN_START_Period)
        IN_FINSH_Period = int(IN_FINSH_Period)
    except:
        if int(IN_START_Period) == TypeError:
            print("올바른 연도를 입력하세요.")
        elif int(IN_FINSH_Period) == TypeError or int(IN_FINSH_Period) < int(IN_START_Period):
            print("올바른 연도를 입력하세요.")
        continue

    if IN_START_Period == 0000:
        print(sprit_line)
        print("프로그램을 종료합니다.")
        print(sprit_line)
        break
    
    Group_Fratio = int(input("검색을 원하는 재무비율 번호를 입력하세요\n 1:유동성  2:수익성  3:안정성  4:성장성"))
    def Search_ratio(index):
        if Group_Fratio == 1:
            print(liquidity_ratio)
            print("\n")
            Search_liquidity_ratio_name = input("검색을 원하는 비율명을 입력하세요.")
            return Search_liquidity_ratio_name
        elif Group_Fratio == 2:
            print(profit_ratio)
            print("\n")
            Search_profit_ratio_name = input("검색을 원하는 비율명을 입력하세요.")
            return Search_profit_ratio_name       
        elif Group_Fratio == 3:
            print(stable_ratio)
            print("\n")
            Search_stable_ratio_name = input("검색을 원하는 비율명을 입력하세요.")
            return Search_stable_ratio_name
        else:
            print(growth_ratio)
            print("\n")
            Search_growth_ratio_name = input("검색을 원하는 비율명을 입력하세요.")
            return Search_growth_ratio_name
    Find_ratio = Search_ratio(Group_Fratio)
    
    "검색을 원하는 재무비율 1: 유동성, 2:수익성, 3:성장성, 4:안정성
    ex) 1. 유동성 선택시 -> 목록 제시, 선택 기능(1개 혹은 전체 혹은 일부) -> 재무비율과 표준비율 비교하는 내용 csv로 저장(파일 이름 = (기업명)AnalyzeREPORT)"
'''