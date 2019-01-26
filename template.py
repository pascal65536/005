# JSON file
file_name = 'causes.json'

# Типы отключений
type_causes = ['авариное', 'аварийное', 'плановое']

# Вывод в файл
output_file = 'causes.html'

# scrapping page
scrap_url = 'http://93.92.65.26/aspx/Gorod.htm'

# Районы города. Пока так
regions = {
    'Центральный',
    'Советский',
    'Свердловский',
    'Октябрьский',
    'Ленинский',
    'Кировский',
    'Железнодорожный'
}

magic_word = 'район'
magic_water_supply = 'водоснабжение'


# Отключенные ресурсы
pictures = {
    'Холодное': 'http://krasnoarsk.ru/wp-content/uploads/2018/11/tap.png',
    'Горячее': 'http://krasnoarsk.ru/wp-content/uploads/2018/11/radiator-1.png',
    'Теплоснабжение': 'http://krasnoarsk.ru/wp-content/uploads/2018/11/radiator-1.png',
    'Электроснабжение': 'http://krasnoarsk.ru/wp-content/uploads/2018/11/bulb.png',
    'Газоснабжение': 'http://krasnoarsk.ru/wp-content/uploads/2018/11/gas.png'
}

# Как будет выглядеть информация об отключении
list_cause = {
    'cause_resource': '<p><b>Что отключат:</b> {}<p>',
    'cause_company': '<p><b>Организация:</b> {}<p>',
    'cause_company_phone': '<p><b>Телефон:</b> {}<p>',
    'address': '<p><b>Адрес отключения:</b> {}<p>',
    'type_cause': '<p><b>Тип отключения:</b> {}<p>',
    'cause': '<p><b>Причина отключений:</b> {}<p>'
}

footer = '<div style="clear: both"></div></body>'

hid_begin = '<div class="indentation" id="comments"><div class="one-news-comments"><div class="row header comments-js" data-show=".comments-block"><h2>'

hid_med ='</h2></div><div class="comments-block"><div class="comment-area">'

hid_end ='</div></div></div></div>'

pic_begin = '<div class="productpic">'

pic_end = '</div>'

style = '<style>.flexbox {display: flex;flex-flow: row wrap;align-items: flex-start;width: 100%; justify-content: left;}.productcard{background-color: #eaeaea;flex-direction: column;justify-content: left;display: flex;border: 0px solid #445162;border-radius: 8px;box-sizing: border-box;width: 300px;margin: 3px;}.productpic {padding: 0px 0px 0px 0px;height: 225px;}.producttext {width: 300px;}</style>'

start = '<p>Узнайте о плановых и неплановых отключениях воды и электроэнергии на сайте ГородскиеНовости.РФ</p><h3>Где в данный момент отключен свет в Красноярске.</h3><p><strong>Информация обновляется ежедневно по мере поступления.</strong></p>'

stop = '<p><img src="http://www.gornovosti.ru/media/filer_public/46/5c/465c2fed-4032-4cde-9205-473c4f94767c/otkliuchenie_vody_i_elektroenergii.jpg"></p>'
