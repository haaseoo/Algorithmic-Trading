import sqlite3

con = sqlite3.connect("kospi.db")
cur = con.cursor()

cur.execute("""CREATE TABLE kakao(Date text, Open int, High int, Low int, Closing int, Volume int)""")
cur.execute("""INSERT INTO kakao VALUES("26.03.19", 97000, 98600, 96900, 98000, 321405)""")
cur.execute("INSERT INTO kakao VALUES('26.03.18', 99000, 99300, 96300, 97500, 556790)")


con.commit()
con.close()