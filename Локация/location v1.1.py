import requests
from bs4 import BeautifulSoup

#settings
HEADERS = {
		'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 YaBrowser/20.3.0.1223 Yowser/2.5 Yptp/1.23 Safari/537.36'
}

#IP
URL2 = 'https://yandex.ru/search/?text=ip&clid=2353473-306&win=426&lr=11342'
response2 = requests.get(URL2, headers = HEADERS)
soup2 = BeautifulSoup(response2.content, 'html.parser')
ip = soup2.find('td', {'class' : 'table__cell', 'scope' : 'col'})
ip = ip.text[4:-4]
print(ip)

#settings_2
URL = 'http://ip2geolocation.com/?ip=' + ip
response = requests.get(URL, headers= HEADERS)
soup = BeautifulSoup(response.content, 'html.parser')

#information
items = soup.findAll('td', class_ = 'cbl')
items = items[1]
things = items.findAll('tr')
print('\n' + things[0].text.replace('д', 'д: ') + '\n')
print(things[1].text.replace('а', 'а: ') + '\n')
print(things[2].text.replace('а', 'а: ') + '\n')
print("\aНажмите любую клавишу, чтобы выйти:")
input()