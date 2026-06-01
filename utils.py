from docxtpl import DocxTemplate
import re

"""удаляю недопустимые знаки в названии файла меняя на нижнее подчеркивание"""
def clean_filename(name: str) -> str:
    return re.sub(r'[<>:"/\\|?*]', '_', name)

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


def edo_context(context):
    doc = DocxTemplate('О Договоре/Шаблоны/ДС замена стороны Договора-ШАБЛОН.docx')
    doc.render(context)
    doc.save("О Договоре/Замена стороны {0}.docx".format(clean_filename(context['abbreviated_name'])))


    doc = DocxTemplate('О Договоре/Шаблоны/Прил №2 Точки поставки - ШАБЛОН.docx')
    doc.render(context)
    doc.save("О Договоре/Прил №2 Точки поставки {0}.docx".format(clean_filename(context['abbreviated_name'])))


    doc = DocxTemplate('О Договоре/Шаблоны/Соглашение ЭДО - ШАБЛОН.docx')
    doc.render(context)
    return doc.save("О Договоре/Соглашение ЭДО {0}.docx".format(clean_filename(context['abbreviated_name'])))

