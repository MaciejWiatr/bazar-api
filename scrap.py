import bs4
import requests
import json


def bazar_search(search):
    url = f'https://bazar.lowcygier.pl/?options=&title={search}&sort=-created_at&per-page=25'
    req = requests.get(url)
    data = req.content
    soup = bs4.BeautifulSoup(data,'html.parser')
    posts = soup.find_all('div', {'class':'game-list'})
    game_list = []

    for game in posts:
        title = game.find('h4',{'class':'media-heading'})
        link = title.find('a')['href']
        price = game.find('p',{'class':'prc'})
        game_title_text = title.text.strip()
        game_link = f'https://bazar.lowcygier.pl{link}'
        game_price = float(price.text.split(' ')[0].replace(',','.'))

        game_info = {
            'name' : game_title_text,
            'price' : game_price,
            'link' : game_link
        }
        
        game_list.append(game_info)
    
    json_list = json.dumps(game_list,indent=4)
    return json_list
