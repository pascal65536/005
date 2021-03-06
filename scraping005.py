from urllib.request import urlopen
from lxml.html import fromstring
from lxml import etree
import json
import template


def clear_string_spaces(string):
    return ' '.join(string.replace(u'\r\n',' ').split())


def clear_all_spaces(lists):
    return_this = []
    for l in lists:
        return_this.append(' '.join(l.split()))
    return return_this


def cause_time(tr_elem):
    ret = tr_elem[2].text_content().split('    ')
    ret = list(map(str.strip, ret))
    if len(ret) == 2:
        return_this = []
        return_this.append(clear_string_spaces(ret[0]))
        return_this.append(clear_string_spaces(ret[1]))
    else:
        return_this = ret
    return clear_all_spaces(return_this)


def cause_address_type(tr_elem):
    this_type = ''
    for type in template.type_causes:
        if type in tr_elem[1].text_content():
            ret = tr_elem[1].text_content().split(type)
            ret = list(map(str.strip, ret))
            this_type = type
    try:
        ret[0] = ret[0].replace(u'\r\n',' ').replace(u',',', ')
        ret[0] = ret[0].strip('- ,.;').strip()
        ret[1] = ret[1].replace(u'\r\n',' ').replace(u',',', ')
        ret[1] = ret[1].strip('- ,.;').strip()
        return_this = ret
        return_this[1:1] = [this_type.capitalize()]
        return clear_all_spaces(return_this)
    except UnboundLocalError:
        pass


def cause_resource(tr_elem):
    ret = tr_elem[0].text_content().split('\xa0')
    ret = tr_elem[0].text_content().split('\r\n')

    ret = list(map(str.strip, ret))

    if len(ret) > 2 and template.magic_water_supply == ret[1]:
        ret.pop(1)
        ret[0] = f'{ret[0]} {template.magic_water_supply}'

    if 'т.' in ret[-1]:
        return_this = [ret[0], ' '.join(ret[1:-1]).strip(), ret[-1].replace(u'т.',' ').strip()]
    else:
        return_this = [ret[0], ' '.join(ret[1:]).strip()]
    return clear_all_spaces(return_this)


def add_new_cause(cause, findregion, tr_elem):
    # Заводим новый словарь
    strn = {}

    # если крайние ячейки пустые, значит это название района или отключений нет или пустая строчка
    if '\xa0' == tr_elem[0].text_content() and '\xa0' == tr_elem[2].text_content():
        # есть название района - значит это название района, иначе - "нет отключений"
        if findregion in tr_elem[1].text_content():
            strn['cause_region'] = clear_string_spaces(tr_elem[1].text_content())
        else:
            strn['cause_out'] = clear_string_spaces(tr_elem[1].text_content())
    # если крайние ячейки не пустые, то это информация об отключении
    else:
        strn['cause_resource'] = cause_resource(tr_elem)[0]
        strn['cause_company'] = cause_resource(tr_elem)[1]
        if len(cause_resource(tr_elem)) > 2:
            strn['cause_company_phone'] = cause_resource(tr_elem)[2]
        if cause_address_type(tr_elem) is not None:
            strn['address'] = cause_address_type(tr_elem)[0]
            strn['type_cause'] = cause_address_type(tr_elem)[1]
            strn['cause'] = cause_address_type(tr_elem)[2]
        if len(cause_time(tr_elem)) == 2:
            strn['begin_time'] = cause_time(tr_elem)[0]
            strn['end_time'] = cause_time(tr_elem)[1]
        else:
            strn['cancel_time'] = cause_time(tr_elem)[0]

    # в первой колонке есть упоминание ресурса, значит этот рерурс отключат
    for pict in template.pictures:
        if pict in tr_elem[0].text_content():
            strn['cause_picture'] = template.pictures[pict]

    # проверим, сколько информации в словаре, если её мало, то словарь не нужен
    s = 0
    for k, v in strn.items():
        s = s + len(v)
    if s > 2:
        cause[findregion].append({'value': strn})

def main(url):

    cause = {}
    find_region = ''

    details_html = urlopen(url).read()
    details_doc = fromstring(details_html)
    
    div_element = details_doc.cssselect('body')[0].getchildren()[6]
    tr_elements = div_element.cssselect('tr')

    for tr in tr_elements:
        for region in template.regions:
            if region in tr.cssselect('td')[1].text_content() and template.magic_word in tr.cssselect('td')[1].text_content():
                find_region = region
                cause[find_region] = []
        if not find_region == '':
            add_new_cause(cause, find_region, tr.cssselect('td'))
    return cause


if __name__ == '__main__':
    scrap = main(template.scrap_url)

    # dump dicts of scrap
    with open(template.file_name, 'w', encoding='utf8') as file_write:
        json.dump(scrap, file_write, indent=4, ensure_ascii=False)
