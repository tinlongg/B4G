import sqlite3 as sq

# creating data to use
def createData():
    data = []

    return data

task_notes = ["Need to work.", "Gotta work.", "No procrastination."]

# database stuff
db = sq.connect("tasks.db")
cur = db.cursor()

try: # only make the db if it doesn't exist alr
    cur.execute("create table notes (note)")
except:
    # add to the database
    for note in task_notes:
        cur.execute("insert into notes values(?)",
            (note,))
        db.commit()

# get data from the database


db.close()