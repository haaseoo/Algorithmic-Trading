# 1. 삼성전자의 PER, PBR 출력
import time
import mojito

with open("secrets/koreainvestment.key", "r", encoding="utf-8") as f:
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

resp = broker.fetch_price("005930")

print("PER: ", resp['output']['per'])   # 시가
print("PBR: ", resp['output']['pbr'])    # 고가



# 2. 삼성전자, LG 전자, SK 하이닉스 종목 코드를 알아낸 후 종목별 시가, 고가, 저가, 종가 출력
stocks = {
    "삼성전자": "005930",
    "LG전자": "066570",
    "SK하이닉스": "000660"
}

print("종목별 시세 조회")

for name, code in stocks.items():
    resp = broker.fetch_price(code)

    if resp['rt_cd'] == '0':
        # 0은 성공, 그 외는 실패
        print(f"\n[ {name} ]")
        print("Open: ", resp['output']['stck_oprc'])  # 시가
        print("High: ", resp['output']['stck_hgpr'])  # 고가
        print("Low: ", resp['output']['stck_lwpr'])  # 저가
        print("Close: ", resp['output']['stck_prpr'])  # 종가
    else:
        print(f"\n[ {name} ] 조회 실패: {resp['msg1']}")

    time.sleep(1)

# 0은 숫자, '0'은 문자 -> 문자열과 비교하기