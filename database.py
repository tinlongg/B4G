import sqlite3

db = sqlite3.connect("task_database.db")
cur = db.cursor()

task_notes = []

# get data from tasks and notes
def addTaskNotes(data):
    task_notes.append(data)

    return task_notes

task_notes = addTaskNotes("")

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

try: # don't create table if it alr exists
    cur.execute("create table notes(note)")
except: # do everything if no error
    # add data to database
    addData()

    # delete from database once user deletes task
    for i in range(len(task_notes)):
        deleteData(task_notes[i])
    
    # get from database
    getData()

    db.close()
