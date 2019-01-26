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
            out.write('<div class="productcard">\n')
            if 'cause_picture' in cause.keys():
                out.write('<div class="productpic">')
                out.write('<img src="{}" class="image" width="300" height="225">'.format(cause['cause_picture']))
                out.write('</div>')
            out.write('<div class="producttext">\n')

            # Тут было нагромождение if, я вынес их в отдельный словарь
            for l in template.list_cause:
                if l in cause.keys():
                    out.write(template.list_cause[l].format(cause[l]))

            if 'cancel_time' in cause.keys():
                out.write('<p><b>{}</b><p>'.format(cause['cancel_time']))
            else:
                if 'begin_time' in cause.keys():
                    out.write('<p><b>Когда отключат:</b> {}<p>'.format(cause['begin_time']))
                if 'end_time' in cause.keys():
                    out.write('<p><b>Когда включат:</b> {}<p>'.format(cause['end_time']))

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
            name = f'{region} {template.magic_word}'
            cause = causes[region]

            # если у района словари содержат одно поле 'cause_region' и остальные поля 'cause_out',
            # то это - район-пустышка
            # считаем сколько строчек содержат 'cause_out'
            count = 0
            for c in cause:
                if c['value'].get('cause_out') is not None:
                    count += 1
            if len(cause) - count > 1:
                write_hide(out, name, cause)

        out.write(template.footer)


if __name__ == '__main__':
    # load dump dicts of scrap
    with open(template.file_name, 'r', encoding='utf-8-sig') as file_read:
        read_scrap = json.load(file_read)

    write_file(read_scrap)
