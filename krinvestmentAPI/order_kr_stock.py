# 1. 잔고 조회
import mojito
# import pprint

key = "key"
secret = "secret"
acc_no = "..-01"

with open("mock.key") as f:
    lines = f.readlines()

broker = mojito.KoreaInvestment(
    api_key=key,
    api_secret=secret,
    acc_no=acc_no,
    mock=True,
)

resp = broker.fetch_balance()
# pprint.pprint(resp)

for comp in resp["output1"]:
    print(comp['pdno'])
    print(comp['prdt_name'])
    print(comp['hldg_qty'])
    print(comp['pchs_ant'])
    print(comp['evlu_amt'])
    print('-'*40)
resp = broker.fetch_balance()
print(resp) # 서버가 보내준 전체 응답을 먼저 확인하세요!
# 2. 매수 주문




# 3. 매도 주문


# 4. 주문 취소


# 5. 주문 정정