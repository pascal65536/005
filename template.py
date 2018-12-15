# Вывод в файл
output_file = 'index.html'

# Адрес, который надо парсить
url = 'http://93.92.65.26/aspx/Gorod.htm'

# Как разделить предприятия
#organizations = ['ООО УК ЖСК', 'ООО Электрические', 'ЭУ', 'Электрические', 'ОАО', 'ПАО', 'КрасТЭК', 'АО', 'ТСЖ', 'СибЭР', 'Часное лицо', 'ООО', 'УК']
organizations = ['ПАО МРСК Сибири', 'ООО КрасТЭК', 'ООО Кульбытстрой', 'МП Горэлектротранс', 'ООО Аквилон', 'МБОУ', 'ООО УК ЖСК', 'ООО Электрические', 'ПАО МРСК Сибири Красноярскэнерго', 'АО КТТК', 'ООО Сервис-техно', 'ООО Электрические сети Сибири', 'ЭУ ООО КрасКом']

# Типы отключений
causes = ['аварийное', 'плановое']

# Районы города. Пока так
region = {
    'Цен': 'Центральный район',
    'Сов': 'Советский район',
    'Св': 'Свердловский район',
    'Окт': 'Октябрьский район',
    'Лен': 'Ленинский район',
    'Кир': 'Кировский район',
    'Жел': 'Железнодорожный район',
    'Окт Жел': 'Октябрьский район',
    'Жел Окт': 'Железнодорожный район',
    'Жел+Окт': 'Железнодорожный район',
    'Жел Цен': 'Железнодорожный район',
    '': ''
}

# Отключенные ресурсы
pictures = {
    'Холодное водоснабжение и Горячее водоснабжение': 'http://krasnoarsk.ru/wp-content/uploads/2018/11/tap.png',
    'Холодное водоснабжение': 'http://krasnoarsk.ru/wp-content/uploads/2018/11/tap.png',
    '': 'http://krasnoarsk.ru/wp-content/uploads/2018/11/tap.png',
    'Горячее водоснабжение Теплоснабжение': 'http://krasnoarsk.ru/wp-content/uploads/2018/11/radiator-1.png',
    'Теплоснабжение': 'http://krasnoarsk.ru/wp-content/uploads/2018/11/radiator-1.png',
    'Теплоснабжение горячее водоснабжение': 'http://krasnoarsk.ru/wp-content/uploads/2018/11/radiator-1.png',
    'Теплоснабжение и горячее': 'http://krasnoarsk.ru/wp-content/uploads/2018/11/radiator-1.png',
    'Теплоснабжение и Горячее водоснабжение': 'http://krasnoarsk.ru/wp-content/uploads/2018/11/radiator-1.png',
    'Теплоснабжение и горячее водоснабжение': 'http://krasnoarsk.ru/wp-content/uploads/2018/11/radiator-1.png',
    'Электроснабжение': 'http://krasnoarsk.ru/wp-content/uploads/2018/11/bulb.png',
    'Газоснабжение': 'http://krasnoarsk.ru/wp-content/uploads/2018/11/gas.png'
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
