import sqlite3
con = sqlite3.connect('surfersDB.sbd')
cur = con.cursor()
cur.execute('''create table surfers(name varchar(20), country varchar(20), average float, board varchar(20), age integer)''')
cur.close()
con.close()
