import io
import sys
import re
import requests
from bs4 import BeautifulSoup
import json
import template


def write_hide(out, name, all_causes):
    '''
    Выводит в html-файл раскрывашку с карточками внутри
    :param out: файл
    :param name: название района
    :param all_causes: список отключений
    :return: ничего
    '''
    out.write(template.hid_begin)
    out.write(name)
    out.write(template.hid_med)

    out.write('<div class="flexbox">\n')
    for all_cause in all_causes:
        if all_cause['ron'] == name:
            out.write('<div class="productcard"><div class="productpic">\n')
            pic = template.pictures[all_cause["res"].strip()]

            out.write(f'<img src="{pic}" class="image" width="300" height="225">')
            out.write('</div><div class="producttext">\n')
            if not all_cause["res"] == "":
                out.write(f'<p><b>Что отключат:</b> {all_cause["res"]}<p>')
                
            out.write(f'<p><b>Организация:</b> {all_cause["org"]}<p>')

            if not all_cause["tel"] == '':
                out.write(f'<p><b>Телефон:</b> {all_cause["tel"]}<p>')

            out.write(f'<p><b>Адреса домов:</b> {all_cause["adr"]}<p>')
            out.write(f'<p><b>Сколько домов:</b> {all_cause["hou"]}<p>')
            out.write(f'<p><b>Причина отключений:</b> {all_cause["cau"]}<p>')
            out.write(f'<p><b>Когда отключат:</b> {all_cause["begin_time"]}<p>')
            out.write(f'<p><b>Когда включат:</b> {all_cause["end_time"]}<p>')

            out.write('</div></div>\n')
    out.write('</div>\n')
    out.write(template.hid_end)


def number(name, all_causes):
    '''
    Есть ли такое название в списке.
    Сколько раз встречается это название в списке.
    :param name: район города
    :param all_causes: список отключений
    :return: количество вхождений
    '''
    num = (name in [all_cause['ron'] for all_cause in all_causes])
    return num

def write_file(all_causes, regions):
    '''
    Вывод в файл
    '''
    with io.open(template.output_file, 'w') as out:
        #out.write(template.header)

        out.write(template.style)
        out.write(template.start)
        for name in regions:
            if not name == '':
                if number(name, all_causes) != 0:
                    write_hide(out, name, all_causes)
        out.write(template.footer)
        #out.write(template.stop)


def my_unwrap(string):
    '''
    Снимаем обёртку
    '''
    for match in string.findAll('span'):
        match.unwrap()
    return string


def begin_end(string):
    '''
    Делим пополам - начало и конец отключений
    '''
    begin_time = ''
    end_time = ''
    if len(string) > 1:
        half = len(string) // 2
        begin_time = string[:half].strip()
        end_time = string[half:].strip()
    return {
        'begin_time': begin_time,
        'end_time': end_time
    }


def cause(string):
    '''
    Разбираем столбец на адреса и причину отключения
    '''
    adr = ''
    cau = ''
    for cause in template.causes:
        if cause in string:
            adr, cau = string.split(cause)
            cau = cause + ' ' + cau
            break
    return {
        'adr': adr,
        'cau': cau
    }


def organization(string):
    '''
    Разбираем столбец на ресурс, который отключают, организацию и её телефон
    '''
    res = ''
    org = ''
    tel = ''
    for organization in template.organizations:
        if organization in string:
            '''
            Разделяем по типу организации. Нужно добавить тип, если что-то поменяется
            '''
            res, organiz = string.split(organization)
            if organiz.find('т.') > 0:
                '''
                Если нет телефона, то городим огород
                '''
                org = organization + ' ' + organiz.split('т.')[0].strip()
                tel = organiz.split('т.')[1].strip()
            else:
                org = (organization + ' ' + organiz).strip()
            break
    return {
        'res': res,
        'org': org,
        'tel': tel
    }


def my_clear(string):
    '''
    Очищаем таблицу. Удаляем лишние символы
    '''
    string = string.get_text()
    string = string.replace("\r","")
    string = string.replace("\n", "")
    string = string.replace("\xa0", " ")
    string = string.replace("   ", " ")
    string = string.replace("  ", " ")
    string = string.replace("  ", " ")
    string = string.strip()
    return string


def create_dict(url):
    '''
    Парсим страницу и создаём словарь отключений
    :param url: ссылка на страницу службы 005
    :return: словарь отключений
    '''
    result = []
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    tables = soup.findAll("table")
    table0 = tables[0]
    i = 0
    for row in table0.findAll("tr"):
        '''
        Разбираем таблицу
        Первые две строки не учитываем
        Там склееные столбцы и название столбцов
        '''
        i += 1
        if i > 1:
            try:
                '''
                1 что и кто отключит
                2 район города
                3 сколько домов отключено
                4 адрес и причина отключений
                5 начало и конец отключений
                '''

                res_org = my_clear(row.findAll("td")[1])
                ron = template.region[my_clear(row.findAll("td")[2])]
                adr_cause = my_clear(row.findAll("td")[4])
                begin_end_time = my_clear(row.findAll("td")[5])

                res = {
                    'ron': ron,
                    'hou': my_clear(row.findAll("td")[3])
                }

                res.update(organization(res_org))
                res.update(cause(adr_cause))
                res.update(begin_end(begin_end_time))

            except IndexError:
                pass
            except KeyError:
                pass
            else:
                '''
                Если района нет, то это пустая ячейка и её надо пропустить
                '''
                if not res['ron'] == '':
                    result.append(res)
    return result


def run():
    all_causes = create_dict(template.url)
    regions = set(template.region.values())
    write_file(all_causes, regions)


if __name__ == '__main__':
    run()
