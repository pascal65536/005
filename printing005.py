import template
import io
import json


def write_hide(out, name, all_cause):
    '''
    Выводит в html-файл раскрывашку с карточками внутри
    :param out: файл
    :param name: название района
    :param all_causes: список отключений
    :return: ничего
    '''
    out.write('\n\n\n')
    out.write(template.hid_begin)
    out.write(name)
    out.write(template.hid_med)
    out.write('\n\n\n')

    out.write('<div class="flexbox">\n')
    out.write('<div class="productcard"><div class="productpic">\n')
    out.write(f'<img src="{all_cause["cause_picture"]}" class="image" width="300" height="225">')
    out.write('</div><div class="producttext">\n')
    out.write(f'<p><b>Что отключат:</b> {all_cause["cause_resource"]}<p>')
    out.write(f'<p><b>Организация:</b> {all_cause["cause_company"]}<p>')
    if 'cause_company_phone' in all_cause.keys():
        out.write(f'<p>{all_cause["cause_company_phone"]}<p>')
    out.write(f'<p><b>Тип отключения:</b> {all_cause["type_cause"]}<p>')
    out.write(f'<p><b>Причина отключений:</b> {all_cause["cause"]}<p>')
    out.write(f'<p><b>Когда отключат:</b> {all_cause["begin_time"]}<p>')
    out.write(f'<p><b>Когда включат:</b> {all_cause["end_time"]}<p>')

    out.write('</div></div>\n')
    out.write('</div>\n')
    out.write(template.hid_end)


def write_file(causes):
    '''
    Вывод в файл
    '''
    with io.open(template.output_file, 'w') as out:
        out.write(template.style)
        out.write(template.start)

        for region in template.regions:
            if len(causes[region][1]['value']) > 1:
                name = causes[region][0]['value']['cause_region'].strip()
                all_causes = causes[region][1]['value']
                write_hide(out, name, all_causes)

        out.write('\n\n\n')
        out.write(template.footer)


if __name__ == '__main__':
    # load dump dicts of scrap
    with open(template.file_name, 'r', encoding='utf-8-sig') as file_read:
        read_scrap = json.load(file_read)

    write_file(read_scrap)
