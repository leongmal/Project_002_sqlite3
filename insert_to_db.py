# insert_to_db.py

import sqlite3
import os
from config_data import company_data

DATABASE = 'employee.db'

def check_table_exists():
    """Проверяет, существует ли таблица employee"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # Используем DESC для надежности, если вдруг есть таблицы с похожими именами
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='employee'")
    exists = cursor.fetchone() is not None
    conn.close()
    return exists

def insert_company(data):
    """Вставляет данные компании в таблицу employee, игнорируя дубликаты по ИНН"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    physical_address = data['legal_address']
    
    try:
        cursor.execute('''
            INSERT OR IGNORE INTO employee (
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
        
        if conn.total_changes > 0:
            print("✅ Данные успешно вставлены в таблицу employee")
        else:
            print(f"⚠️ Запись пропущена. Компания с ИНН {data.get('inn')} уже существует.")
            
    except sqlite3.Error as e:
        print(f"❌ Ошибка БД: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    if not os.path.exists(DATABASE):
        print(f"⚠️ База данных {DATABASE} не найдена...")
    elif not check_table_exists():  # Теперь Python знает об этой функции
        print("⚠️ Таблица employee не существует...")
    else:
        insert_company(company_data)