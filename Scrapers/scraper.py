import requests
import lxml.html as html
import os
import datetime

HOME_URL = 'https://www10.animeflv.cc/browse'
HOME_URL2 = 'https://www10.animeflv.cc'

#XPATH_LINK_DIRECTORY='//nav[@class="CX Row"]/ul[@class="Menu"]/li[last()]/a/@href'

XPATH_LINK_TO_ANIME='//main[@class="Main"]/ul[@class="ListAnimes AX Rows A03 C02 D02"]/li/article[@class="Anime alt B"]/a/@href'

XPATH_TITLE='//div[@class="Container"]/h2[@class="Title"]/text()'

XPATH_SYNOPSIS='//div[@class="Container"]/div[@class="BX Row BFluid Sp20"]/main[not(@class)]/section[@class="WdgtCn"]/div[@class="Description"]/text()'

XPATH_CATEGORIES='//div[@class="Container"]/div[@class="BX Row BFluid Sp20"]/main[not(@class)]/section[@class="WdgtCn"]/nav[@class="Nvgnrs"]/a/text()'

XPATH_TYPE='//div[@class="Container"]/span[@class="Type movie" or @class="Type tv"]/text()'

def parse_anime(links, today):
    try:
        response = requests.get(links)
        if response.status_code == 200:
            anime = response.content.decode('utf-8')
            parsed = html.fromstring(anime)

            try:
                title = parsed.xpath(XPATH_TITLE)[0]
                title = title.replace('\"', '')
                print(title)
                description = parsed.xpath(XPATH_SYNOPSIS)[0]
                print(description)
                categories = parsed.xpath(XPATH_CATEGORIES)
                print(categories)
                type_anime = parsed.xpath(XPATH_TYPE)[0]
                print(type_anime)
            except IndexError:
                return
            
            with open(f'{today}/{title}.txt', 'w', encoding='utf-8') as f:
                f.write(title)
                f.write('\n\n')
                f.write(description)
                f.write('\n\n')
                f.write(type_anime)
                f.write('\n\n')
                for p in categories:
                    f.write(p)
                    f.write('\n')
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)


def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links_to_animes = parsed.xpath(XPATH_LINK_TO_ANIME)
            # print(links_to_animes)

            today = datetime.date.today().strftime('%d-%m-%Y')
            if not os.path.isdir(today):
                os.mkdir(today)
            for link in links_to_animes:
                links = HOME_URL2 + link
                print(links)
                parse_anime(links, today)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)

def run():
    parse_home()


if __name__ == '__main__':
    run()