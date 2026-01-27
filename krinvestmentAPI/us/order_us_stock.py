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
        exchange='나스닥',
        mock=True
)

# 현재가
price = broker.fetch_price("TSLA")
pprint.pprint(price)

# 지정가 매수
resp = broker.create_limit_buy_order(
    symbol="TQQQ",
    price=30,
    quantity=5,
)
pprint.pprint(resp)

# 지정가 매도
resp = broker.create_limit_sell_order(
    symbol="TQQQ",
    price=30,
    quantity=5,
)
pprint.pprint(resp)