from flask import Flask, render_template, request, flash, get_flashed_messages, redirect, url_for
import sqlite3
import os
from utils import date_str

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
            inn INTEGER NOT NULL,
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
    dict_thomas_of_property ={'АО':'Акционерное Общество','ООО':'Общество с ограниченной отвественностью',
                              'ПАО':'Публичное Акционерное Общество','ИП':'Индивидуальный предприниматель'}

    try:
        cursor.execute("SELECT * FROM employee WHERE id = ?", (employee_id,))
        employee = cursor.fetchone()

        if not employee:
            flash('Договор не найден','error')
            return redirect(url_for('index'))
        
        ## путь для сохр файла
        output_dir = 'О Договоре'
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
            f.write(f' {employee[2]}\n')     # date_contract (индекс 2) вступает в силу с ..
            f.write(f"31.12.2026 года\n")
            f.write(f"АРБП\n")
            f.write(f'{employee[12]}\n')     # legal_address (индекс 12) Юр адрес
            f.write(f'{employee[13]}\n')     # psihical_address (индекс 13) Физ адрес
            f.write(f'{employee[16]}\n')     # inn (индекс 16) ИНН потреб
            f.write(f'{employee[17]}\n')     # kpp (индекс 17) КПП потреб
            f.write(f'{employee[18]}\n')     # ogrn (индекс 18) ОГРН потреб
            f.write(f'{employee[21]}\n')     # current_account(индекс 21) Расч счет потреб
            f.write(f'{employee[22]}\n')     # bank (индекс 22) БАНК потреб
            f.write(f'{employee[23]}\n')     # correspondent_account (индекс 23) Коресп счет
            f.write(f'{employee[24]}\n')     # bik (индекс 3) БИК
            f.write(f'{employee[15]}\n')     # tlf (индекс 15) Контактный телефон
            f.write('\n\n\n')
            f.write('Данные для Соглашения ЭДО\n')
            f.write('=' * 30 + '\n')
            f.write(f"Публичное Акционерное Общество \"{employee[4]}\"\n")    
            f.write(f'{dict_thomas_of_property[employee[3]]} \"{employee[4]}\"\n')         
            f.write(f'Сокращенное фирменное наименование Общества: {employee[3]} \"{employee[5]}\"\n')     # thomas_of_property (индекс 3) Форма организации
            f.write(f'Юридический адрес: {employee[12]}\n')     # legal_address (индекс 12) Юр адрес
            f.write(f'Фактический адрес: {employee[13]}\n')     # psihical_address (индекс 13) Физ адрес
            f.write(f'ИНН {employee[16]}  КПП {employee[17]}\n')     # psihical_address (индекс 13) ИНН КПП
            f.write(f'ОГРН {employee[18]}\n')     # ogrn (индекс 18) ОГРН потреб
            f.write(f'ОКВЭД {employee[19]}\n')     # okved (индекс 19) ОКВЭД потреб
            f.write(f'ОКПО {employee[20]}\n')     # okpo (индекс 20) ОКПО потреб
            f.write(f"Банковские реквизиты:\n")
            f.write(f'Расчетный счет {employee[21]}\n')     # current_account(индекс 21) Расч счет потреб
            f.write(f'{employee[22]}\n')     # bank (индекс 22) БАНК потреб
            f.write(f'Кор. счет {employee[23]}\n')     # correspondent_account (индекс 23) Коресп счет
            f.write(f'БИК {employee[24]}\n')     # bik (индекс 3) БИК
            f.write(f'Контактный телефон {employee[15]}\n')     # phone_namber (индекс 15) Контактный телефон
            f.write('\n\n\n')
            f.write(f'{employee[3]} \"{employee[5]}\"\n') 
            f.write(f'{employee[9]}\n')     # position (индекс 9) Должность
            f.write(f'/{employee[6]}/\n')     # fio (индекс 6) Фамилия Имя Отчество
            f.write('\n\n\n')
            f.write(f'{employee[27]}\n')     # fioedo (индекс 27) ФИО ЭДО
            f.write(f'{employee[28]}\n')     # emailedo (индекс 28) Почта ЭДО
            f.write(f'{employee[29]}\n')     # telephonedo (индекс 29) Тлф ЭДО
            f.write(f'{employee[30]}\n')     # operatoredo (индекс 30) Оператор ЭДО
            f.write('\n\n\n')
            f.write(f'{dict_thomas_of_property[employee[3]]} \"{employee[4]}\" (сокращенное фирменоое наименование {employee[3]} \"{employee[5]}\", в лице {employee[10]} {employee[8]}, действующего на основании {employee[11]}')
            




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
