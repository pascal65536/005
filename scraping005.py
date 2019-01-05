from urllib.request import urlopen
from lxml.html import fromstring
import json
import datetime
import os


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


def main(url):
    
    cause = {}
    causes = []
    n = 0
    r = ''

    details_html = urlopen(url).read()
    details_doc = fromstring(details_html)
    
    div_element = details_doc.cssselect('body')[0].getchildren()[6]
    tr_elements = div_element.cssselect('tr')

    for tr in tr_elements:
        for region in regions:
            if region in tr.cssselect('td')[1].text_content():
                r = region
                cause[r] = {}

        if not r == '' and len(tr.text_content()) > 20:
            n = n + 1

            cause[r][n] = {}
            cause[r][n]['res'] = tr.cssselect('td')[0].text_content()
            cause[r][n]['adr'] = tr.cssselect('td')[1].text_content()
            cause[r][n]['tim'] = tr.cssselect('td')[2].text_content()

    causes.append(cause)
    print(causes)
    print(len(cause))

    # dump dicts of airlines
    with open('causes.json', 'w', encoding='utf8') as file_dump:
        json.dump(causes, file_dump, indent=2, ensure_ascii=False)



if __name__ == '__main__':
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
    
    main(scrap_url)


