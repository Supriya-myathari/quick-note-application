from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Create database
def init_db():
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS notes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        note TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/save", methods=["POST"])
def save_note():
    data = request.get_json()
    note = data["note"]

    conn = sqlite3.connect("notes.db")
    c = conn.cursor()

    c.execute("INSERT INTO notes(note) VALUES(?)", (note,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Saved Successfully"})


@app.route("/notes")
def get_notes():

    conn = sqlite3.connect("notes.db")
    c = conn.cursor()

    c.execute("SELECT note FROM notes ORDER BY id DESC")

    notes = [row[0] for row in c.fetchall()]

    conn.close()

    return jsonify(notes)


if __name__ == "__main__":
    app.run(debug=True)