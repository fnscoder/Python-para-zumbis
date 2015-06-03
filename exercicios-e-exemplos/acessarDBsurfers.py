import sqlite3
con = sqlite3.connect('surfersDB.sbd')
cur = con.cursor()

#cur.execute('''insert into surfers values("Felipe Souza", "Brazil", 9.5, "Free style", 30)''')
#cur.execute('''insert into surfers values("Lucas Souza", "Brazil", 7.5, "Free style", 13)''')
#cur.execute('''insert into surfers values("Danielle Souza", "Brazil", 8.5, "Free style", 32)''')
cur.execute('''select * from surfers''')
cur.execute('''select * from surfers where age > 10 order by average desc''')

for x in cur.fetchall():
    print(x)

cur.close()
con.commit()
con.close()
