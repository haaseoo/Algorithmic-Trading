import pandas as pd
import yfinance as yf
import sqlite3

df = yf.download(
    "MU",
    start="2016-03-27",
    end="2026-03-27",
    auto_adjust=False,
    progress=False
)

print(df.head())

con = sqlite3.connect("/Users/anhaseo/Desktop/haaseo/py/Algorithmic-Trading/unit17/stocks.db")

df.to_sql("MU", con, if_exists="replace")

readed_df = pd.read_sql(
    'SELECT * FROM "MU"',
    con,
    index_col="Date",
    parse_dates=["Date"]
)

print(readed_df.head())

con.close()