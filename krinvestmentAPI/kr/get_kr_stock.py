# 1. 증권사 객체 생성
import mojito
import pprint

with open("../secrets/koreainvestment.key", "r", encoding="utf-8") as f:
    lines = f.readlines()

    key = lines[0].strip()
    secret = lines[1].strip()
    acc_no = lines[2].strip()

    broker = mojito.KoreaInvestment(
        api_key=key,
        api_secret=secret,
        acc_no=acc_no,
        mock=True
)

# print(broker)

# 삼성전자 조회
resp = broker.fetch_price("005930")
# pprint.pprint(resp)

print("Open: ", resp['output']['stck_oprc'])   # 시가
print("High: ", resp['output']['stck_hgpr'])    # 고가
print("Low: ", resp['output']['stck_lwpr'])     # 저가
print("Close: ", resp['output']['stck_prpr'])    # 종가


# 종목코드 조회
symbols = broker.fetch_symbols()
# print(symbols)
print("----- 주권만 필터링 ----- ")
print(symbols[ symbols['그룹코드'] == 'ST'])

print("----- 코스피 필터링 ----- ")
symbols = broker.fetch_kospi_symbols()
print(symbols.head())

print("----- 코스닥 필터링 ----- ")
symbols = broker.fetch_kosdaq_symbols()
print(symbols.head())