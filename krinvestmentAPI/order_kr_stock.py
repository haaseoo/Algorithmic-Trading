# 1. 잔고 조회
import mojito
import pprint
import time

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

# 2. 매수 주문
# broker = mojito.KoreaInvestment(api_key=key, api_secret=secret, acc_no=acc_no)
time.sleep(0.5)

# 지정가
resp = broker.create_limit_buy_order(
    symbol="005930",
    price=100000,
    quantity=1
)
pprint.pprint(resp)

# 시장가
resp = broker.create_market_buy_order(
    symbol="005930",
    quantity=10
)
pprint.pprint(resp)


# 매도 주문
# 지정가
resp = broker.create_limit_sell_order(
    symbol="005930",
    price=100000,
    quantity=1
)
pprint.pprint(resp)

# 시장가
resp = broker.create_market_sell_order(
    symbol="005930",
    quantity=10
)
pprint.pprint(resp)


# 주문 취소
# 전체 취소
resp = broker.cancel_order(
    org_no="91252",
    order_no="0000119206",
    quantity=4,  # 잔량전부 취소시 원주문 수량과 일치해야함
    total=True   # 잔량 전부
)
pprint.pprint(resp)

# 일부 취소
resp = broker.cancel_order(
    org_no="",
    order_no="",
    quantity=2,  # 취소하고자 하는 수량
    total=False   # 잔량 일부
)
pprint.pprint(resp)


# 주문 정정
resp = broker.modify_order(
    org_no="",
    order_no="",
    order_type="00",
    price=60000,
    quantity=4,
    total=True
)
pprint.pprint(resp)