import requests 
from bs4 import BeautifulSoup 
import time 

url = 'https://cgr.qoldau.kz/ru/checkpoint/list/224751327844000000/view' # Адрес сайта для отслеживания 
sleep_time = 60 # Время между проверками в секундах 

# Начало бесконечного цикла мониторинга 
while True: 
    response = requests.get(url) 
    soup = BeautifulSoup(response.content, 'html.parser') 
    html_result = soup.find_all('div', {'class': 'zag-level-5'}) 
    
    print(f'Found total days: {len(html_result)}') 
    for elm in html_result:
        # print(elm['data-original-title'])
        tmp_list = list(elm.attrs.values());
        dateDay = tmp_list[2].split('<br><b>')[0]
        availability = tmp_list[2].split('<br><b>')[1].split('</b>')[0]
        print(f'Day: {dateDay} | {availability}')

    
    # Ожидание перед следующей проверкой 
    time.sleep(sleep_time)