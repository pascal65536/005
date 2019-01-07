import template
import io
import json


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


def write_file(causes):
    '''
    Вывод в файл
    '''
    with io.open(template.output_file, 'w') as out:
        out.write(template.style)
        out.write(template.start)

        print( causes['Октябрьский'][1] )

        #for region in template.regions:
        #    print ( region )

        '''
        for name in regions:
            if not name == '':
                if number(name, all_causes) != 0:
                    write_hide(out, name, all_causes)
        '''
        out.write('\n\n\n')
        out.write(template.footer)


if __name__ == '__main__':
    # load dump dicts of scrap
    with open(template.file_name, 'r', encoding='utf-8-sig') as file_read:
        read_scrap = json.load(file_read)

    write_file(read_scrap)
