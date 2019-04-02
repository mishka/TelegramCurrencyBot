# -*- coding: utf-8 -*-
import re, csv, json, tweepy, datetime, subprocess
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
base_url = "https://www.xe.com/currencyconverter/convert/?Amount=1&From={}&To=TRY"

def current_time():
    return str(datetime.datetime.now().strftime('%H:%M'))

def tweet():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    start_t = datetime.datetime.now()
    c_data = get_data()
    end_t = datetime.datetime.now() - start_t
    print("\nTook {} to execute.\n\n{}".format(str(end_t)[:7], c_data))
    api.update_status(status = c_data)
    print("Tweet sent!")

def browser(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options = chrome_options)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    rate = soup.find('span', {'class' : 'converterresult-toAmount'})
    return re.sub('[^0-9,.]', '', str(rate))

def perc(x):
    if "-" in x:
        well = '📉 ' + x[:5] + '%'
    else:
        well = '📈 ' + x[:4] + '%'
    return well

def compare(old, current):
    percentage = 100 * (float(current) - float(old)) / float(old)
    list = []
    list.append(percentage)
    return ''.join(str(e) for e in list)

def jsonrw(which, current):
    with open("rates.json", "r+") as x:
        data = json.load(x)
        old = data[which]
        data[which] = current
        x.seek(0)
        json.dump(data, x, indent = 4, sort_keys = True)
        x.truncate()
        x.close()
    return perc(compare(old, current))

def update_csv():
    with open('chart.csv', 'a') as f:
        with open("rates.json", "r") as x:
            fwrite = csv.writer(f)
            data = json.load(x)
            fwrite.writerow([current_time(), data['gbp'], data['eur'], data['usd'], data['cad'], data['qar'], data['rub'], data['cny'], data['jpy'], data['krw']])
            f.close()
            x.close()
    print('Updated csv!')

def get_data():
    return "{}\n\n{}{}{}{}{}{}{}{}{}".format(current_time(), gbp(), eur(), usd(), cad(), qar(), cny(), rub(), jpy(), krw()) 

def gbp():
    print("Fetching gbp data..")
    gbp_current = browser(base_url.format("GBP"))
    return "🇬🇧 £1 = ₺{} > {}\n".format(gbp_current[:-3], jsonrw("gbp", gbp_current))

def eur():
    print("Fetching eur data..")
    eur_current = browser(base_url.format("EUR"))
    return "🇪🇺 €1 = ₺{} > {}\n".format(eur_current[:-3], jsonrw("eur", eur_current))

def usd():
    print("Fetching usd data..")
    usd_current = browser(base_url.format("USD"))
    return "🇺🇸 $1 = ₺{} > {}\n".format(usd_current[:-3], jsonrw("usd", usd_current))

def cad():
    print("Fetching cad data..")
    cad_current = browser(base_url.format("CAD"))
    return "🇨🇦 C$1 = ₺{} > {}\n".format(cad_current[:-3], jsonrw("cad", cad_current))

def qar():
    print("Fetching qar data..")
    qar_current = browser(base_url.format("QAR"))
    return "🇶🇦 QR1 = ₺{} > {}\n".format(qar_current[:-3], jsonrw("qar", qar_current))

def rub():
    print("Fetching rub data..")
    rub_current = browser(base_url.format("RUB"))
    return "🇷🇺 ₽1 = ₺{} > {}\n".format(rub_current[:-4], jsonrw("rub", rub_current))

def cny():    
    print("Fetching cny data..")
    cny_current = browser(base_url.format("CNY"))
    return "🇨🇳 ¥1 = ₺{} > {}\n".format(cny_current[:-4], jsonrw("cny", cny_current))

def jpy():
    print("Fetching jpy data..")
    jpy_current = browser(base_url.format("JPY"))
    return "🇯🇵 ¥1 = ₺{} > {}\n".format(jpy_current[:-4], jsonrw("jpy", jpy_current))

def krw():
    print("Fetching krw data..")
    krw_current = browser(base_url.format("KRW"))
    return "🇰🇷 ₩1 = ₺{} > {}\n".format(krw_current[:-4], jsonrw("krw", krw_current))

while True:
    try:
        day_of_week = datetime.date.today().weekday()
        time_now = datetime.datetime.now().time()

        if day_of_week < 5 and (time_now > datetime.time(9,40) and time_now < datetime.time(18,15)):
            tweet()
            update_csv()
            print("Done, sleeping for 13 minutes.") # it takes about 2 mins to fetch the data on avg
            sleep(780)
        else:
            print("Outside of working hours, hibernating..")
            sleep(1800)
    except Exception as e:
        print(str(e))
        subprocess.call("killall chrome && killall chromedriver", shell = True)
        sleep(10)
        tweet()
        sleep(780)
