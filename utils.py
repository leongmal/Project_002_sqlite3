def date_str(str_dt):
    monh_dict = {
        "01":"января", "02":"февраля","03":"марта",
        "04":"апреля", "05":"мая", "06":"июня",
        "07":"июля", "08":"августа", "09":"сентября",
        "10":"октября","11":"ноября", "12":"декабря"
    }
    list_date = str_dt.split('.')
    day, monh, year = list_date
    return f"{day} {monh_dict[monh]} {year}"


#     print(f"{day} {monh_dict[monh]} {year}")

# date_str('01.02.2026')
