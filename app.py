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
            number_contract TEXT NOT NULL,
            date_contract TEXT NOT NULL,
            thomas_of_property TEXT NOT NULL,
            name_of_the_organization TEXT NOT NULL,
            abbreviated_name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Извлекаем данные напрямую из формы
        number_contract = request.form['number_contract']
        date_contract = request.form['date_contract']
        thomas_of_property = request.form['thomas_of_property']
        name_of_the_organization = request.form['name_of_the_organization']
        abbreviated_name = request.form['abbreviated_name']

        # name = request.form['name']
        # age = request.form['age']

        # Отладка: проверяем типы и значения
        # print(f"Inserting: {number_contract}, {date_contract}, {name}, {age}")
        # print(f"Types: {type(number_contract)}, {type(name)}, {type(age)}")

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO employie (number_contract, date_contract, thomas_of_property, name_of_the_organization, abbreviated_name) VALUES (?, ?, ?, ?, ?)",
                (number_contract, date_contract, thomas_of_property, name_of_the_organization, abbreviated_name)
            )
            conn.commit()
            print("Record inserted successfully")
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()
        finally:
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
