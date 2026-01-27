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

ohlcv = broker.fetch_ohlcv(
    symbol="TSLA",
    timeframe='D',
    adj_price=True
)
pprint.pprint(ohlcv)