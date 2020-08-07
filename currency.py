import datetime as dt
import re, csv, json, subprocess

from time import sleep
from requests import post
from urllib.parse import quote as qt

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHAT_ID = '-1001362458728'
TOKEN = ''
BASE_URL = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From={}&To=TRY'
SELECTOR = '#converterResult > div > div > div.converterresult-conversionTo > span.converterresult-toAmount'

CURRENCY_DICT = (
    ('GBP', 3, '🇬🇧 £1 = ₺{} > {}'),
    ('EUR', 3, '🇪🇺 €1 = ₺{} > {}'),
    ('USD', 3, '🇺🇸 $1 = ₺{} > {}'),
    ('CAD', 3, '🇨🇦 $1 = ₺{} > {}'),
    ('JPY', 4, '🇯🇵 ¥1 = ₺{} > {}')
)


def telegram(text):
    post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={qt(text)}&parse_mode=markdown')


def browser(url):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--dns-prefetch-disable')
    options.add_argument('--disable-setuid-sandbox')

    driver = webdriver.Chrome(options = options)

    driver.get(url)
    rate = driver.find_element_by_css_selector(SELECTOR).text
    driver.quit()
    
    return re.sub('[^0-9,.]', '', rate)


def perc(string):
    return f'📉 {string[:5]}%' if '-' in string else f'📈 {string[:4]}%'


def current_time():
    return str(dt.datetime.now().strftime('%H:%M:%S'))


def compare(old, current):
    return str(100 * (current - old) / old)


def update_csv():
    with open('chart.csv', 'a') as csv_file:
        with open('rates.json', 'r') as json_file:
            data = json.load(json_file)
            csv.writer(csv_file).writerow([ current_time(), data['GBP'], data['EUR'], data['CAD'], data['JPY'] ])


def db(target, current):
    with open('rates.json', 'r+') as json_file:
        data = json.load(json_file)

        old = data[target]
        data[target] = current
        
        json_file.seek(0)
        json.dump(data, json_file, indent = 4, sort_keys = True)
    
    return perc(compare(float(old), float(current)))


def fetch_data():
    result = ''

    start_t = dt.datetime.now()

    for currency, crop, string in CURRENCY_DICT:
        print(f'| {current_time()} | Fetching {currency} information...')
        
        rate = browser(BASE_URL.format(currency))
        result += string.format(rate[:-crop], db(currency, rate)) + '\n'
    
    end_t = str(dt.datetime.now() - start_t)[:7]
    print(f'\n| {current_time()} | Took {end_t} to fetch the data.\n\n{result}\n')

    return result


while(1):
    try:
        day_of_week = dt.date.today().weekday()
        time_now = dt.datetime.now().time()

        if (day_of_week < 5 and (time_now > dt.time(9,40) and time_now < dt.time(18,15))):
            telegram(fetch_data())
            print('Done, sleeping for an hour.') # it takes about 2 mins to fetch the data on avg
            sleep(3500)
        else:
            telegram(fetch_data())
            print('Outside of working hours, hibernating..')
            sleep(1800)
    except Exception as e:
        print(f'| {current_time()} |\n{str(e)}')
        subprocess.call('killall chrome && killall chromedriver', shell = True)
        sleep(180)