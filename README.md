# Quick Note Application

A simple single-page note-taking web application built using **Flask**, **SQLite**, **HTML**, **CSS**, and **JavaScript**. Users can write notes, save them to a SQLite database, and view all saved notes on the same page without refreshing.

---

## Features

* Write and save notes
* Store notes in a SQLite database
* Display saved notes dynamically
* Single-page application
* Simple and responsive user interface

---

## Technologies Used

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python (Flask)
* **Database:** SQLite

---

## Project Structure

```text
quick-note-app/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
├── .gitignore
└── README.md
```

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/quick-note-app.git
```

2. Open the project folder:

```bash
cd quick-note-app
```

3. Install Flask:

```bash
pip install flask
```

4. Run the application:

```bash
python app.py
```

5. Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## How It Works

1. Enter a note in the text area.
2. Click the **Save Note** button.
3. The note is sent to the Flask backend.
4. Flask stores the note in a SQLite database.
5. The saved notes are displayed instantly on the same page.

---

## Future Enhancements

* Edit existing notes
* Delete notes
* Search notes
* User authentication
* Categories and tags
* Dark mode

---

## Author

**Supriya Chinnu**

GitHub: https://github.com/YOUR_USERNAME

LinkedIn: https://www.linkedin.com/in/YOUR_LINKEDIN_USERNAME/

---

## License

This project is created for learning and educational purposes.
