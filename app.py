import  Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize DB
def init_db():
    conn = sqlite3.connect("task_database.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS notes (note TEXT)")
    conn.commit()
    conn.close()

init_db()

# Route to serve the main page
@app.route("/")
def index():
    return render_template("index.html")  # must be in templates/ folder

# API to add a note
@app.route("/add_note", methods=["POST"])
def add_note():
    data = request.json
    note = data.get("note")
    conn = sqlite3.connect("task_database.db")
    c = conn.cursor()
    c.execute("INSERT INTO notes (note) VALUES (?)", (note,))
    conn.commit()
    conn.close()
    return jsonify({"status": "success"})

# API to get notes
@app.route("/get_notes", methods=["GET"])
def get_notes():
    conn = sqlite3.connect("task_database.db")
    c = conn.cursor()
    c.execute("SELECT note FROM notes")
    notes = [row[0] for row in c.fetchall()]
    conn.close()
    return jsonify(notes)

# API to delete note
@app.route("/delete_note", methods=["POST"])
def delete_note():
    data = request.json
    note = data.get("note")
    conn = sqlite3.connect("task_database.db")
    c = conn.cursor()
    c.execute("DELETE FROM notes WHERE note = ?", (note,))
    conn.commit()
    conn.close()
    return jsonify({"status": "deleted"})

if __name__ == "__main__":
    app.run(debug=True)
