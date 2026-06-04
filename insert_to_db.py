# insert_to_db.py
import sqlite3
import os
from config_data import company_data

DATABASE = 'employee.db'   # путь к вашей БД

def insert_company(data):
    """Вставляет данные компании в таблицу employee"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # physical_address = legal_address
    physical_address = data['legal_address']
    
    try:
        cursor.execute('''
            INSERT INTO employee (
                number_contract,
                date_contract,
                thomas_of_property,
                name_of_the_organization,
                abbreviated_name,
                fio,
                fioabbr,
                rpfio,
                position,
                rpposition,
                regulation,
                legal_address,
                physical_address,
                mail,
                phone_number,
                inn,
                kpp,
                ogrn,
                okved,
                okpo,
                current_account,
                bank,
                correspondent_account,
                bik,
                benefit,
                additionally,
                fioedo,
                emailedo,
                telephonedo,
                operatoredo
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            data['number_contract'],
            data['date_contract'],
            data['thomas_of_property'],
            data['name_of_the_organization'],
            data['abbreviated_name'],
            data['fio'],
            data['fioabbr'],
            data['rpfio'],
            data['position'],
            data['rpposition'],
            data['regulation'],
            data['legal_address'],
            physical_address,
            data['mail'],
            data['phone_number'],
            data['inn'],
            data['kpp'],
            data['ogrn'],
            data['okved'],
            data['okpo'],
            data['current_account'],
            data['bank'],
            data['correspondent_account'],
            data['bik'],
            data['benefit'],
            data['additionally'],
            data['fioedo'],
            data['emailedo'],
            data['telephonedo'],
            data['operatoredo']
        ))
        conn.commit()
        print("✅ Данные успешно вставлены в таблицу employee")
    except sqlite3.IntegrityError as e:
        print(f"❌ Ошибка целостности: {e}")
        conn.rollback()
    except sqlite3.Error as e:
        print(f"❌ Ошибка БД: {e}")
        conn.rollback()
    finally:
        conn.close()

def check_table_exists():
    """Проверяет, существует ли таблица employee"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='employee'")
    exists = cursor.fetchone() is not None
    conn.close()
    return exists

if __name__ == "__main__":
    if not os.path.exists(DATABASE):
        print(f"⚠️ База данных {DATABASE} не найдена. Сначала создайте её через ваше Flask-приложение или init_db().")
    elif not check_table_exists():
        print("⚠️ Таблица employee не существует. Запустите init_db() из вашего app.py.")
    else:
        insert_company(company_data)

###DELETE FROM employee WHERE id = 17; 