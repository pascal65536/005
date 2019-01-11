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
    out.write('\n\n\n')
    out.write(template.hid_begin)
    out.write(name)
    out.write(template.hid_med)
    out.write('\n\n\n')
    out.write('<div class="flexbox">\n')
    for all_cause in all_causes:
        if len(all_cause['value']) > 1:
            cause = all_cause['value']
            out.write('<div class="productcard"><div class="productpic">\n')
            out.write(f'<img src="{cause["cause_picture"]}" class="image" width="300" height="225">')
            out.write('</div><div class="producttext">\n')
            out.write(f'<p><b>Что отключат:</b> {cause["cause_resource"]}<p>')
            out.write(f'<p><b>Организация:</b> {cause["cause_company"]}<p>')
            if 'cause_company_phone' in cause.keys():
                out.write(f'<p><b>Телефон:</b> {cause["cause_company_phone"]}<p>')
            out.write(f'<p><b>Тип отключения:</b> {cause["type_cause"]}<p>')
            out.write(f'<p><b>Причина отключений:</b> {cause["cause"]}<p>')
            if 'cancel_time' in cause.keys():
                out.write(f'<p><b>{cause["cancel_time"]}</b><p>')
            else:
                out.write(f'<p><b>Когда отключат:</b> {cause["begin_time"]}<p>')
                out.write(f'<p><b>Когда включат:</b> {cause["end_time"]}<p>')

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
            name = f'{region} район'
            all_causes = causes[region]

            # если у района два словаря, а второй содержит поле 'cause_out', то это район-пустышка
            if not (len(all_causes) == 2 and 'cause_out' in all_causes[1]['value'].keys()):
                write_hide(out, name, all_causes)

        out.write(template.footer)


if __name__ == '__main__':
    # load dump dicts of scrap
    with open(template.file_name, 'r', encoding='utf-8-sig') as file_read:
        read_scrap = json.load(file_read)

    write_file(read_scrap)
