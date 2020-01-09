import bs4
import requests
import json


def bazar_search(search):
    url = f'https://bazar.lowcygier.pl/?options=&title={search}&sort=-rating&per-page=100'
    req = requests.get(url)
    data = req.content
    soup = bs4.BeautifulSoup(data.decode('utf-8', 'ignore'), 'html.parser')
    posts = soup.find_all('div', {'class': 'game-list'})
    game_list = []

    for game in posts:
        try:
            title = game.find('h4', {'class': 'media-heading'})
            link = title.find('a')['href']
            price = game.find('p', {'class': 'prc'})
            img = game.find('img', {'class': 'game-image'})['src']
            number_of_offers = int(
                game.find('p', {'class': 'prc-text'}).text[0])
            tags = game.find('div', {'class': 'trader'}
                             ).text.strip().split(',')
            tags = [tag.strip() for tag in tags]
            game_title_text = title.text.strip()
            game_link = f'https://bazar.lowcygier.pl{link}'
            game_price = float(price.text.split(' ')[0].replace(',', '.'))

            game_info = {
                'name': game_title_text,
                'price': game_price,
                'link': game_link,
                'tags': tags,
                'img': img.strip(),
                'number_of_offers': number_of_offers}

            game_list.append(game_info)
        except:
            pass

    json_list = json.dumps(game_list, indent=4,
                           ensure_ascii=False).encode('utf8')
    return json_list
