import sqlite3

DATABASE = 'employee.db'

def employees():
    """Выводит список организаций (ваша исходная логика)"""
    try:
        with sqlite3.connect(DATABASE) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            # Проверяем наличие таблицы перед запросом
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='employee'")
            if not cursor.fetchone():
                print("Таблица 'employee' не найдена.")
                return

            cursor.execute("SELECT id, name_of_the_organization FROM employee ORDER BY name_of_the_organization ASC")
            rows = cursor.fetchall()

            if not rows:
                print("В таблице нет записей.")
                return

            print(f"{'ID':<5} | {'Название организации'}")
            print("-" * 40)
            for row in rows:
                print(f"{row[0]:<5} | {row[1]}")
                
    except sqlite3.Error as e:
        print(f"Ошибка при чтении БД: {e}")

def delete_employee_by_id():
    """Запрашивает ID и удаляет строку из базы"""
    del_id_str = input('Строку с каким ID будем удалять? ')
    
    # Защита от некорректного ввода (буквы, пустой ввод)
    try:
        del_id = int(del_id_str)
    except ValueError:
        print("Ошибка: введено не число. Удаление отменено.")
        return

    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            
            # Сначала проверим, есть ли вообще такая строка (опционально, для красивого вывода)
            cursor.execute("SELECT name_of_the_organization FROM employee WHERE id = ?", (del_id,))
            result = cursor.fetchone()

            if not result:
                print(f"Запись с ID {del_id} не найдена.")
                return

            # Выполняем удаление. Используем параметризованный запрос (?), чтобы избежать SQL-инъекций.
            cursor.execute("DELETE FROM employee WHERE id = ?", (del_id,))
            
            # Метод .rowcount показывает, сколько строк было реально затронуто запросом
            if cursor.rowcount > 0:
                # Изменения автоматически сохраняются при выходе из блока 'with', но commit можно вызвать явно
                conn.commit() 
                print(f"Запись с ID {del_id} («{result[0]}») успешно удалена.")
            else:
                print("Произошла неизвестная ошибка, ничего не удалено.")

    except sqlite3.Error as e:
        print(f"Ошибка базы данных при удалении: {e}")

if __name__ == '__main__':
    while True:
        print("\nВыберите действие:")
        print("1 — Показать все организации")
        print("2 — Удалить организацию по ID")
        print("0 — Выход")
        
        choice = input("Ваш выбор: ")

        if choice == '1':
            employees()
        elif choice == '2':
            delete_employee_by_id()
        elif choice == '0':
            print("Работа программы завершена.")
            break
        else:
            print("Неверный пункт меню. Попробуйте снова.")