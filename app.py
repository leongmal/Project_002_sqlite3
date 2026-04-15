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
            abbreviated_name TEXT NOT NULL,
            fio TEXT NOT NULL,
            fioabbr TEXT NOT NULL,
            rpfio TEXT NOT NULL,
            position TEXT NOT NULL,
            rpposition TEXT NOT NULL,
            regulation TEXT NOT NULL,
            legal_address TEXT NOT NULL,
            physical_address TEXT NOT NULL,
            mail TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            inn INTEGER NOT NULL,
            kpp INTEGER NOT NULL,
            ogrn INTEGER NOT NULL,
            okved INTEGER NOT NULL,
            okpo INTEGER NOT NULL,
            current_account INTEGER NOT NULL,
            bank TEXT NOT NULL,
            correspondent_account INTEGER NOT NULL,
            bik INTEGER NOT NULL,
            benefit TEXT NOT NULL,
            additionally TEXT NOT NULL,
            fioedo TEXT NOT NULL,
            emailedo TEXT NOT NULL,
            telephonedo TEXT NOT NULL,
            operatoredo TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Извлекаем данные напрямую из формы
        number_contract= request.form['number_contract'],
        date_contract= request.form['date_contract'],
        thomas_of_property= request.form['thomas_of_property'],
        name_of_the_organization= request.form['name_of_the_organization'],
        abbreviated_name= request.form['abbreviated_name'],
        fio= request.form['fio'],
        fioabbr= request.form['fioabbr'],
        rpfio= request.form['rpfio'],
        position= request.form['position'],
        rpposition= request.form['rpposition'],
        regulation= request.form['regulation'],
        legal_address= request.form['legal_address'],
        physical_address= request.form['physical_address'],
        mail= request.form['mail'],
        phone_number= request.form['phone_number'],
        inn= request.form['inn'],
        kpp= request.form['kpp'],
        ogrn= request.form['ogrn'],
        okved= request.form['okved'],
        okpo= request.form['okpo'],
        current_account= request.form['current_account'],
        bank= request.form['bank'],
        correspondent_account= request.form['correspondent_account'],
        bik= request.form['bik'],
        benefit= request.form['benefit'],
        additionally= request.form['additionally'],
        fioedo= request.form['fioedo'],
        emailedo= request.form['emailedo'],
        telephonedo= request.form['telephonedo'],
        operatoredo= request.form['operatoredo']

        # Отладка: проверяем типы и значения
        # print(f"Inserting: {number_contract}, {date_contract}, {name}, {age}")
        # print(f"Types: {type(number_contract)}, {type(name)}, {type(age)}")

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO employie (number_contract, date_contract, thomas_of_property, name_of_the_organization, abbreviated_name, fio, fioabbr, rpfio, position, rpposition, regulation, legal_address, physical_address, mail, phone_number, inn, kpp, ogrn, okved, okpo, current_account, bank, correspondent_account, bik, benefit, additionally, fioedo, emailedo, telephonedo, operatoredo) \
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (number_contract, date_contract, thomas_of_property, name_of_the_organization, abbreviated_name, fio, fioabbr, rpfio, position, rpposition, regulation, legal_address, physical_address, mail, phone_number, inn, kpp, ogrn, okved, okpo, current_account, bank, correspondent_account, bik, benefit, additionally, fioedo, emailedo, telephonedo, operatoredo)
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
