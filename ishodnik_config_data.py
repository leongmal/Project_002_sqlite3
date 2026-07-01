# config_data.py
# Исходные данные для вставки в таблицу employee формирует deepseek


company_data = {
    
    "number_contract": "92100-655ЭА",
    "date_contract": "11.09.2023",          # можно поменять на "2023-09-11" при необходимости
    "thomas_of_property": "ООО",
    "name_of_the_organization": "Морские технологии движения",
    "abbreviated_name": "ООО «ММТ»",
    
    "fio": "Марченко Павел Юрьевич",
    "fioabbr": "Марченко П.Ю.",
    "rpfio": "Марченко Павла Юрьевича",
    "position": "Генеральный директор",
    "rpposition": "генерального директора",
    "regulation": "Устава",
     
    "legal_address": "198097, г. Санкт-Петербург, пр-кт Стачек д.47 стр.17 помещ.2-Н ком.75",
    # physical_address будет равен legal_address (см. вставку)
    
    
    "mail": "info@mmt.spb.ru",
    "phone_number": "+7 (812) 702-03-72",
    
    # Реквизиты 
    "inn": "7805808876",
    "kpp": 780501001,
    "ogrn": 1237800098942,
    "okved": "25.99.26",
    "okpo": "48273434",    
    "current_account": "40702810200000154168",
    "bank": "БАНК ГПБ (АО) 117420 г Москва ул Наметкина д.16 /1",
    "correspondent_account": "30101810200000000823",
    "bik": "044525823",
    
    # Дополнительная информация
    "benefit": "",
    "additionally": "",  # из инф.txt нет дополнительных контактных лиц, кроме ответственного за ЭДО
    
    # ЭДО 
    "fioedo": "Шевчукова Алеся Сергеевна",
    "emailedo": "AlSShevchukova@mmt.spb.ru",
    "telephonedo": "+79112242813",
    "operatoredo": "Контур Диадок",
}
