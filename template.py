# JSON file
file_name = 'causes.json'

# Типы отключений
type_causes = ['авариное', 'аварийное', 'плановое', 'плаовое']

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
    'Холодное': 'http://krasnoarsk.ru/media/icons/tap.png',
    'Горячее': 'http://krasnoarsk.ru/media/icons/radiator-1.png',
    'Теплоснабжение': 'http://krasnoarsk.ru/media/icons/radiator-1.png',
    'Электроснабжение': 'http://krasnoarsk.ru/media/icons/bulb.png',
    'Газоснабжение': 'http://krasnoarsk.ru/media/icons/gas.png'
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

start = '<link rel="stylesheet" href="static/font.css"><link rel="stylesheet" href="static/reset.css"><link rel="stylesheet" href="static/main.css"><link rel="stylesheet" href="static/extra.css"><script src="static/jquery-3.2.1.min.js"></script><script src="static/slick.min.js"></script><script src="static/main.js"></script><h3>Где в данный момент отключен свет в Красноярске.</h3>'

stop = '<p>&nbsp;</p>'
