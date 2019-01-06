from urllib.request import urlopen
from lxml.html import fromstring
from lxml import etree
import json
import datetime
import os
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
    

def write_file(all_causes, regions):
    '''
    Вывод в файл
    '''
    with io.open(template.output_file, 'w') as out:
        out.write(template.style)
        out.write(template.start)
        for name in regions:
            if not name == '':
                if number(name, all_causes) != 0:
                    write_hide(out, name, all_causes)
        out.write(template.footer)


def main(url):
    
    cause = {}
    causes = []
    n = 0
    find_region = ''

    details_html = urlopen(url).read()
    details_doc = fromstring(details_html)
    
    div_element = details_doc.cssselect('body')[0].getchildren()[6]
    tr_elements = div_element.cssselect('tr')

    for tr in tr_elements:
        for region in template.regions:
            if region in tr.cssselect('td')[1].text_content():
                find_region = region
                cause[find_region] = {}
        if not find_region == '' and len(tr.text_content()) > 20:
            n = n + 1
            cause[find_region][n] = {}
            cause[find_region][n]['cause_resource'] = tr.cssselect('td')[0].text_content().replace(u'\r\n',' ')
            cause[find_region][n]['cause_address'] = tr.cssselect('td')[1].text_content().replace(u'\r\n',' ')
            cause[find_region][n]['time_start_end'] = tr.cssselect('td')[2].text_content().replace(u'\r\n',' ')
            for pict in template.pictures:
                if pict in tr.cssselect('td')[0].text_content():
                    cause[find_region][n]['cause_picture'] = template.pictures[pict]

    causes.append(cause)


if __name__ == '__main__':
    scrap = main(template.scrap_url)

    file_name = 'causes.json'

    # dump dicts of scrap
    with open(file_name, 'w') as file_write:
        json.dump(scrap, file_write, indent=2)

    with open(file_name, 'r') as file_read:
        read_scrap = json.load(file_read)

    print(scrap == read_scrap)

'''
            res = tr.cssselect('td')[0]
            #print(res.text_content())
            #for fnt in res.cssselect('font'):
            #    print(fnt.text_content())
            #print(len(res), res.xpath("string()"))
            if len(res) > 0:
                #print(9, res.text_content())
                #print(1, res[1].text_content().strip())
'''
