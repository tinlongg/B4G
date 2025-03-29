# sqlite
import sqlite3 as sq

name = "Ezinne"
age = 19
year = "Freshman"

db = sq.connect("practice.db")

cur = db.cursor()

try: # only make the db if it doesn't exist alr
    cur.execute("create table students(name, age, year)")
except:
    cur.execute("insert into students (name, age, year) values (?, ?, ?)",
            (name, age, year))
    db.commit()

# my_name = cur.execute("select name from students where name = 'Ezinne'")

'''for data in my_name.fetchall():
    print(data[0])'''

cur.execute("delete from students where name = 'Ezinne'")

for row in cur:
    print(row)

db.close()