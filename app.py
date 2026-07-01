from flask import Flask, render_template, request, flash, get_flashed_messages, redirect, url_for
import sqlite3
import os
from utils import date_str, edo_context

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Путь к базе данных
DATABASE = 'employee.db'

def init_db():
    """Создание таблицы при необходимости"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employee (
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
            inn TEXT NOT NULL,
            kpp INTEGER NOT NULL,
            ogrn INTEGER NOT NULL,
            okved TEXT NOT NULL,
            okpo TEXT NOT NULL,
            current_account TEXT NOT NULL,
            bank TEXT NOT NULL,
            correspondent_account TEXT NOT NULL,
            bik TEXT NOT NULL,
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
        number_contract= request.form['number_contract']
        date_contract= request.form['date_contract']
        thomas_of_property= request.form['thomas_of_property']
        name_of_the_organization= request.form['name_of_the_organization']
        abbreviated_name= request.form['abbreviated_name']
        fio= request.form['fio']
        fioabbr= request.form['fioabbr']
        rpfio= request.form['rpfio']
        position= request.form['position']
        rpposition= request.form['rpposition']
        regulation= request.form['regulation']
        legal_address= request.form['legal_address']
        physical_address= request.form['physical_address']
        mail= request.form['mail']
        phone_number= request.form['phone_number']
        inn= request.form['inn']
        kpp= request.form['kpp']
        ogrn= request.form['ogrn']
        okved= request.form['okved']
        okpo= request.form['okpo']
        current_account= request.form['current_account']
        bank= request.form['bank']
        correspondent_account= request.form['correspondent_account']
        bik= request.form['bik']
        benefit= request.form['benefit']
        additionally= request.form['additionally']
        fioedo= request.form['fioedo']
        emailedo= request.form['emailedo']
        telephonedo= request.form['telephonedo']
        operatoredo= request.form['operatoredo']


        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO employee (number_contract, date_contract, thomas_of_property, name_of_the_organization, abbreviated_name, fio, fioabbr, rpfio, position, rpposition, regulation, legal_address, physical_address, mail, phone_number, inn, kpp, ogrn, okved, okpo, current_account, bank, correspondent_account, bik, benefit, additionally, fioedo, emailedo, telephonedo, operatoredo) \
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (number_contract, date_contract, thomas_of_property, name_of_the_organization, abbreviated_name, fio, fioabbr, rpfio, position, rpposition, regulation, legal_address, physical_address, mail, phone_number, inn, kpp, ogrn, okved, okpo, current_account, bank, correspondent_account, bik, benefit, additionally, fioedo, emailedo, telephonedo, operatoredo)
            )
            conn.commit()
            flash('Данные внесены в базу!', 'success')
            print("Record inserted successfully")
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()
            flash('Ошибка при сохранении данных', 'error') 
        finally:
            conn.close()
    #     return render_template("index.html")
    # return render_template("index.html")

    messages = get_flashed_messages(with_categories=True)
    return render_template("index.html", messages=messages)

@app.route('/employees')
def employees():
    with sqlite3.connect(DATABASE) as conn:
        conn.row_factory = sqlite3.Row  # Для доступа по именам колонок
        cursor = conn.cursor()

        # прверка сущ таблицы
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='employee'")
        if not cursor.fetchone():
            flash('Таблица employee не найдена в базе данных')
            # return render_template('employees.html',employees=[])
                       
        # сотировка по id 
        # cursor.execute("SELECT * FROM employee")
        # вывод с сортировкой по имени 
        cursor.execute("SELECT * FROM employee ORDER BY name_of_the_organization ASC")
        employees = cursor.fetchall()

        # conn.close()
    return render_template('employees.html', employees=employees)


## Логика загрузки данных для редактирования
@app.route('/edit/<int:employee_id>', methods=['GET', 'POST'])
def edit_employee(employee_id):
    # Подключение к базе данных
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        # Получаем данные текущего договора из БД
        cursor.execute("SELECT * FROM employee WHERE id = ?", (employee_id,))
        employee = cursor.fetchone()

        if employee is None:
            flash('Договор с указанным ID не найден', 'error')
            return redirect('/employees')

        if request.method == 'POST':
            # Извлекаем данные из формы
            number_contract = request.form['number_contract']
            date_contract = request.form['date_contract']
            thomas_of_property = request.form['thomas_of_property']
            name_of_the_organization = request.form['name_of_the_organization']
            abbreviated_name = request.form['abbreviated_name']
            fio = request.form['fio']
            fioabbr = request.form['fioabbr']
            rpfio = request.form['rpfio']
            position = request.form['position']
            rpposition = request.form['rpposition']
            regulation = request.form['regulation']
            legal_address = request.form['legal_address']
            physical_address = request.form['physical_address']
            mail = request.form['mail']
            phone_number = request.form['phone_number']
            inn = request.form['inn']
            kpp = request.form['kpp']
            ogrn = request.form['ogrn']
            okved = request.form['okved']
            okpo = request.form['okpo']
            current_account = request.form['current_account']
            bank = request.form['bank']
            correspondent_account = request.form['correspondent_account']
            bik = request.form['bik']
            benefit = request.form['benefit']
            additionally = request.form['additionally']
            fioedo = request.form['fioedo']
            emailedo = request.form['emailedo']
            telephonedo = request.form['telephonedo']
            operatoredo = request.form['operatoredo']


            # Обновляем запись в базе данных
            cursor.execute('''
                UPDATE employee
                SET number_contract = ?, date_contract = ?, thomas_of_property = ?,
                    name_of_the_organization = ?, abbreviated_name = ?, fio = ?,
                    fioabbr = ?, rpfio = ?, position = ?, rpposition = ?,
                    regulation = ?, legal_address = ?, physical_address = ?,
                    mail = ?, phone_number = ?, inn = ?, kpp =?, ogrn =?, okved = ?,
                    okpo = ?, current_account =?, bank =?, correspondent_account =?, 
                    bik =?, benefit = ?, additionally = ?, fioedo = ?, emailedo = ?,
                    telephonedo = ?, operatoredo = ?     
                WHERE id = ?
                ''', (
                number_contract, date_contract, thomas_of_property,
                name_of_the_organization, abbreviated_name, fio,
                fioabbr, rpfio, position, rpposition,
                regulation, legal_address, physical_address,
                mail, phone_number, inn, kpp, ogrn, okved, okpo,
                current_account, bank, correspondent_account, bik,
                benefit, additionally, fioedo, emailedo, telephonedo, operatoredo,
                employee_id, 
            ))
            conn.commit()

            flash('Данные договора успешно обновлены!', 'success')
            return redirect('/employees')

        # Если метод GET — отображаем форму с текущими данными
        return render_template('edit_employee.html', employee=dict(employee))

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        flash('Ошибка при работе с базой данных', 'error')
        return redirect('/employees')
    finally:
        conn.close()




@app.route('/print/<int:employee_id>', methods =['POST'])
def print_employee(employee_id):
    # Подключение к БД  для печати в text
    conn = sqlite3.connect(DATABASE)
    # conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    dict_thomas_of_property ={'АО':'Акционерное Общество','ООО':'Общество с ограниченной ответственностью',
                              'ПАО':'Публичное Акционерное Общество','ИП':'Индивидуальный предприниматель'}

    try:
        cursor.execute("SELECT * FROM employee WHERE id = ?", (employee_id,))
        employee = cursor.fetchone()

        if not employee:
            flash('Договор не найден','error')
            return redirect(url_for('index'))
        
        ## путь для сохр файла
        output_dir = 'О Договоре/result'
        os.makedirs(output_dir, exist_ok=True)

        filename = f'{employee_id}.txt'
        filepath = os.path.join(output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('Данные для договора\n')
            f.write('=' * 30 + '\n')
            f.write(f'№{employee[1]}\n')      # number_contract Номер 
            f.write(f'{date_str(employee[2])}г.\n') # дата переведена в "01 января 2026г.""
            f.write(f'{dict_thomas_of_property[employee[3]]}\n')             
            f.write(f'{employee[3]}\n')     # thomas_of_property (индекс 3) Форма организации
            f.write(f'"{employee[4]}"\n')     # name_of_the_organization(индекс 4) Наименование орг
            f.write(f'"{employee[5]}"\n')     # abbreviated_name(индекс 5) Сокращенн наим орг
            f.write(f'{employee[9]}\n')     # position (индекс 9) Должность
            f.write(f'{employee[7]}\n')     # fioabbr (индекс 7) Фамилия И.О
            f.write(f'{employee[10]}\n')     # rpposition (индекс 10) Должность р.п.
            f.write(f'{employee[8]}\n')     # rpfio (индекс 8 Фамилия Имя Отчество р.п.
            f.write(f'{employee[11]}\n')     # regulation (индекс 11) дейтв. на оновании
            f.write(f'{employee[14]}\n')     # mail (индекс 14) почта потреб
            f.write(f"office@es.kzgroup.ru\n")
            f.write(f' {employee[2]}\n')     # date_contract (индекс 2) вступает в силу с ..
            f.write(f"31.12.2026 года\n")
            f.write(f"АРБП\n")
            f.write(f'{employee[12]}\n')     # legal_address (индекс 12) Юр адрес
            f.write(f'{employee[13]}\n')     # psihical_address (индекс 13) Физ адрес
            f.write(f'{employee[16]}\n')     # inn (индекс 16) ИНН потреб
            f.write(f'{employee[17]}\n')     # kpp (индекс 17) КПП потреб
            f.write(f"'{employee[18]}\n")     # ogrn (индекс 18) ОГРН потреб
            f.write(f"'{employee[21]}\n")     # current_account(индекс 21) Расч счет потреб
            f.write(f'{employee[22]}\n')     # bank (индекс 22) БАНК потреб
            f.write(f"'{employee[23]}\n")     # correspondent_account (индекс 23) Коресп счет
            f.write(f"'{employee[24]}\n")     # bik (индекс 3) БИК
            f.write(f'{employee[15]}\n')     # tlf (индекс 15) Контактный телефон
            
        context = {'number_contract': employee[1],
                   'date_contract' : date_str(employee[2]),
                   'date' : employee[2],
                   'thomas_of_property_full' : dict_thomas_of_property[employee[3]],
                   'thomas_of_property' : employee[3],
                   'name_of_the_organization' : employee[4],
                   'abbreviated_name' : employee[5],
                   'rpposition' : employee[10],
                   'rpfio' : employee[8],
                   'regulation' : employee[11],
                   'operatoredo' : employee[30],
                   'fioedo' : employee[27],
                   'telephonedo' : employee[29],
                   'emailedo' : employee[28],
                   'legal_address' : employee[12],
                   'psihical_address' : employee[13],
                   'inn' : employee[16],
                   'kpp' : employee[17],
                   'ogrn' : employee[18],
                   'okved' : employee[19],
                   'okpo' : employee[20],
                   'current_account' : employee[21],
                   'bank' : employee[22],
                   'correspondent_account' : employee[23],
                   'bik' : employee[24],
                   'phone_number' : employee[15],
                   'position' : employee[9],
                   'fio' : employee[6],
                   'fioabbr' : employee[7]
                   }  
        edo_context(context)



        flash(f'Данные для Договора {employee_id} сохранены в {filename}', 'success')

    except Exception as e:
        flash(f'Ошибка при сохранении: {str(e)}', 'error')
    finally:
        conn.close()

    return redirect(url_for('index'))  # перенаправляем обратно на главную    


if __name__ == '__main__':
    # Инициализируем базу данных при запуске
    init_db()
    app.run(debug=True)
