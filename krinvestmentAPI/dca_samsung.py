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
# print(key)
# print(secret)
# print(acc_no)

balance = broker.fetch_balance()
deposit = int(balance['output2'][0]['dnca_tot_amt'])
print(deposit)

SYMBOL = '005930'
price = broker.fetch_price(symbol=SYMBOL)
cur_price = int(price['output']['stck_prpr'])
print(cur_price)

QUANTITY = 1
if cur_price < deposit:
    broker.create_market_buy_order(symbol=SYMBOL, quantity=QUANTITY)