# 1. 잔고 조회
import mojito
import pprint

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

resp = broker.fetch_balance()
# pprint.pprint(resp)

# 보유 종목 : 키 값으로 보유 종목에 대한 정보 확인
resp = broker.fetch_balance()
holdings = resp['output1']

if len(holdings) == 0:
    print("현재 보유 중인 종목이 없습니다.")
else:
    print(f"총 {len(holdings)}개의 종목을 보유 중입니다. \n")

    for comp in resp['output1']:
        print(comp['pdno'])
        print(comp['prdt_name'])
        print(comp['hldg_qty'])
        print(comp['pchs_amt'])
        print(comp['evlu_amt'])
        print("-" * 20)