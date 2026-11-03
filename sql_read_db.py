import sqlite3

DATABASE = 'employee.db'

with sqlite3.connect(DATABASE) as conn:
    cursor = conn.cursor()
    
    query = "SELECT abbreviated_name, number_contract, id FROM employee"
    
    try:
        cursor.execute(query)
        
        column_names = [description[0] for description in cursor.description]
        print("\t".join(column_names))
        print("-" * 80)
        
        rows = cursor.fetchall()
        
        if not rows:
            print("Таблица пуста.")
        else:
            for row in rows:
                print("\t".join(str(item) for item in row))
                
    except sqlite3.OperationalError as e:
        print(f"Ошибка выполнения запроса: {e}")