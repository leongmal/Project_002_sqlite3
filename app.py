from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

# Путь к базе данных
DATABASE = 'employie.db'

def init_db():
    """Создание таблицы при необходимости"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employie (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # id = request.form['id']
        name = request.form['name']
        age = request.form['age']

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO employie (name, age) VALUES ( ?, ?)", ( name, age))
        conn.commit()
        conn.close()
        return render_template("index.html")

    return render_template("index.html")

@app.route('/employies')
def employies():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Для доступа по именам колонок
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employie")
    employies = cursor.fetchall()

    conn.close()
    return render_template('employies.html', employies=employies)

if __name__ == '__main__':
    # Инициализируем базу данных при запуске
    init_db()
    app.run(debug=True)
