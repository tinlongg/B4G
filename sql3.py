import sqlite3
db = sqlite3.connect("whiplash.db")

cur = db.cursor()


task_notes = ["Note 1", "Note 2", "Note 3"]

# get data from tasks and notes
def get():
    data = []

    task_notes = []

    task_notes.append(data)

    return task_notes

def addData():
    for i in range(len(task_notes)):
        cur.execute("insert into notes values (?)", (task_notes[i],))
        db.commit()

def getData():
    note_list = cur.execute("select note from notes")

    for data in note_list.fetchall():
        print(data[0])

def deleteData(data):
    cur.execute("delete from notes where note = ?", (data,))
    db.commit()

try:
    cur.execute("create table notes(note)")
except:
    # add data to database
    addData()

    # delete from database
    ''''
    for i in range(len(task_notes)):
        deleteData(task_notes[i])
    '''
    # get from database
    getData()

    db.close()
