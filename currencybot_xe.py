# -*- coding: utf-8 -*-
import re, datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

timex = datetime.datetime.now().strftime('%H:%M')
print(timex + "\n")

chrome_options = Options()
chrome_options.add_argument("--headless")

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

def tweet():
    import tweepy

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    datax = get_data()

    api.update_status(status = datax)
    print("Tweet sent!")

def get_data():
    gbpx = gbp()
    eurx = eur()
    usdx = usd()
    ilsx = ils()
    cnyx = cny()
    rubx = rub()
    iskx = isk()
    jpyx = jpy()
    krwx = krw()

    data = "{}\n\n{}{}{}{}{}{}{}{}{}".format(timex, gbpx, eurx, usdx, ilsx, cnyx, rubx, iskx, jpyx, krwx) 
    print(data)
    return data

def gbp():
    print("Fetching gbp data..")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=GBP&To=TRY")
    gbp_data = driver.page_source
    driver.quit()
    gbp_soup = BeautifulSoup(gbp_data, 'html.parser')
    gbp_rate = gbp_soup.find('span', {'class' : 'converterresult-toAmount'})
    gbp_current = re.sub('[^0-9,.]', '', str(gbp_rate))
    gbp_tweet = gbp_current[:-3]
    
    with open("gbp.txt", "r+") as txt:
        old = txt.readlines()
        old = re.sub('[^.0-9]', '', str(old))
        txt.truncate(0)
        txt.close()

    with open("gbp.txt", "r+") as txt:
        txt.write(gbp_current)
        txt.close()

    current = float(gbp_current)
    old = float(old)
    percentage = 100 * (current - old) / old
    list = []
    list.append(percentage)
    string = ''.join(str(e) for e in list)

    if "-" in string:
        well = '📉 ' + string[:5] + '%'
    else:
        well = '📈 ' + string[:4] + '%'

    gbp_final = "🇬🇧 £1 = ₺{} > {}\n".format(gbp_tweet, well)
    return gbp_final

def eur():
    print("Fetching eur data..")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=TRY")
    eur_data = driver.page_source
    driver.quit()
    eur_soup = BeautifulSoup(eur_data, 'html.parser')
    eur_rate = eur_soup.find('span', {'class' : 'converterresult-toAmount'})
    eur_current = re.sub('[^0-9,.]', '', str(eur_rate))
    eur_tweet = eur_current[:-3]
    
    with open("eur.txt", "r+") as txt:
        old = txt.readlines()
        old = re.sub('[^.0-9]', '', str(old))
        txt.truncate(0)
        txt.close()

    with open("eur.txt", "r+") as txt:
        txt.write(eur_current)
        txt.close()

    current = float(eur_current)
    old = float(old)
    percentage = 100 * (current - old) / old
    list = []
    list.append(percentage)
    string = ''.join(str(e) for e in list)

    if "-" in string:
        well = '📉 ' + string[:5] + '%'
    else:
        well = '📈 ' + string[:4] + '%'

    eur_final = "🇪🇺 €1 = ₺{} > {}\n".format(eur_tweet, well)
    return eur_final

def usd():    
    print("Fetching usd data..")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=TRY")
    usd_data = driver.page_source
    driver.quit()
    usd_soup = BeautifulSoup(usd_data, 'html.parser')
    usd_rate = usd_soup.find('span', {'class' : 'converterresult-toAmount'})
    usd_current = re.sub('[^0-9,.]', '', str(usd_rate))
    usd_tweet = usd_current[:-3]
    

    with open("usd.txt", "r+") as txt:
        old = txt.readlines()
        old = re.sub('[^.0-9]', '', str(old))
        txt.truncate(0)
        txt.close()

    with open("usd.txt", "r+") as txt:
        txt.write(usd_current)
        txt.close()

    current = float(usd_current)
    old = float(old)
    percentage = 100 * (current - old) / old
    list = []
    list.append(percentage)
    string = ''.join(str(e) for e in list)

    if "-" in string:
        well = '📉 ' + string[:5] + '%'
    else:
        well = '📈 ' + string[:4] + '%'

    usd_final = "🇺🇸 $1 = ₺{} > {}\n".format(usd_tweet, well)
    return usd_final

def ils():    
    print("Fetching ils data..")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=ILS&To=TRY")
    ils_data = driver.page_source
    driver.quit()
    ils_soup = BeautifulSoup(ils_data, 'html.parser')
    ils_rate = ils_soup.find('span', {'class' : 'converterresult-toAmount'})
    ils_current = re.sub('[^0-9,.]', '', str(ils_rate))
    ils_tweet = ils_current[:-3]

    with open("ils.txt", "r+") as txt:
        old = txt.readlines()
        old = re.sub('[^.0-9]', '', str(old))
        txt.truncate(0)
        txt.close()

    with open("ils.txt", "r+") as txt:
        txt.write(ils_current)
        txt.close()

    current = float(ils_current)
    old = float(old)
    percentage = 100 * (current - old) / old
    list = []
    list.append(percentage)
    string = ''.join(str(e) for e in list)

    if "-" in string:
        well = '📉 ' + string[:5] + '%'
    else:
        well = '📈 ' + string[:4] + '%'

    ils_final = "🇮🇱 ₪1 = ₺{} > {}\n".format(ils_tweet, well)
    return ils_final

def rub():    
    print("Fetching rub data..")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=RUB&To=TRY")
    rub_data = driver.page_source
    driver.quit()
    rub_soup = BeautifulSoup(rub_data, 'html.parser')
    rub_rate = rub_soup.find('span', {'class' : 'converterresult-toAmount'})
    rub_current = re.sub('[^0-9,.]', '', str(rub_rate))
    rub_tweet = rub_current[:-4]
    
    with open("rub.txt", "r+") as txt:
        old = txt.readlines()
        old = re.sub('[^.0-9]', '', str(old))
        txt.truncate(0)
        txt.close()

    with open("rub.txt", "r+") as txt:
        txt.write(rub_current)
        txt.close()

    current = float(rub_current)
    old = float(old)
    percentage = 100 * (current - old) / old
    list = []
    list.append(percentage)
    string = ''.join(str(e) for e in list)

    if "-" in string:
        well = '📉 ' + string[:5] + '%'
    else:
        well = '📈 ' + string[:4] + '%'

    rub_final = "🇷🇺 ₽1 = ₺{} > {}\n".format(rub_tweet, well)
    return rub_final

def cny():    
    print("Fetching cny data..")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=CNY&To=TRY")
    cny_data = driver.page_source
    driver.quit()
    cny_soup = BeautifulSoup(cny_data, 'html.parser')
    cny_rate = cny_soup.find('span', {'class' : 'converterresult-toAmount'})
    cny_current = re.sub('[^0-9,.]', '', str(cny_rate))
    cny_tweet = cny_current[:-4]
    
    with open("cny.txt", "r+") as txt:
        old = txt.readlines()
        old = re.sub('[^.0-9]', '', str(old))
        txt.truncate(0)
        txt.close()

    with open("cny.txt", "r+") as txt:
        txt.write(cny_current)
        txt.close()

    current = float(cny_current)
    old = float(old)
    percentage = 100 * (current - old) / old
    list = []
    list.append(percentage)
    string = ''.join(str(e) for e in list)

    if "-" in string:
        well = '📉 ' + string[:5] + '%'
    else:
        well = '📈 ' + string[:4] + '%'

    cny_final = "🇨🇳 ¥1 = ₺{} > {}\n".format(cny_tweet, well)
    return cny_final

def jpy():
    print("Fetching jpy data..")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=JPY&To=TRY")
    jpy_data = driver.page_source
    driver.quit()
    jpy_soup = BeautifulSoup(jpy_data, 'html.parser')
    jpy_rate = jpy_soup.find('span', {'class' : 'converterresult-toAmount'})
    jpy_current = re.sub('[^0-9,.]', '', str(jpy_rate))
    jpy_tweet = jpy_current[:-4]
    
    with open("jpy.txt", "r+") as txt:
        old = txt.readlines()
        old = re.sub('[^.0-9]', '', str(old))
        txt.truncate(0)
        txt.close()

    with open("jpy.txt", "r+") as txt:
        txt.write(jpy_current)
        txt.close()

    current = float(jpy_current)
    old = float(old)
    percentage = 100 * (current - old) / old
    list = []
    list.append(percentage)
    string = ''.join(str(e) for e in list)

    if "-" in string:
        well = '📉 ' + string[:5] + '%'
    else:
        well = '📈 ' + string[:4] + '%'

    jpy_final = "🇯🇵 ¥1 = ₺{} > {}\n".format(jpy_tweet, well)
    return jpy_final

def krw():
    print("Fetching krw data..")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=KRW&To=TRY")
    krw_data = driver.page_source
    driver.quit()
    krw_soup = BeautifulSoup(krw_data, 'html.parser')
    krw_rate = krw_soup.find('span', {'class' : 'converterresult-toAmount'})
    krw_current = re.sub('[^0-9,.]', '', str(krw_rate))
    krw_tweet = krw_current[:-4]
    
    with open("krw.txt", "r+") as txt:
        old = txt.readlines()
        old = re.sub('[^.0-9]', '', str(old))
        txt.truncate(0)
        txt.close()

    with open("krw.txt", "r+") as txt:
        txt.write(krw_current)
        txt.close()

    current = float(krw_current)
    old = float(old)
    percentage = 100 * (current - old) / old
    list = []
    list.append(percentage)
    string = ''.join(str(e) for e in list)

    if "-" in string:
        well = '📉 ' + string[:5] + '%'
    else:
        well = '📈 ' + string[:4] + '%'

    krw_final = "🇰🇷 ₩1 = ₺{} > {}\n".format(krw_tweet, well)
    return krw_final

def isk():
    print("Fetching isk data..")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=ISK&To=TRY")
    isk_data = driver.page_source
    driver.quit()
    isk_soup = BeautifulSoup(isk_data, 'html.parser')
    isk_rate = isk_soup.find('span', {'class' : 'converterresult-toAmount'})
    isk_current = re.sub('[^0-9,.]', '', str(isk_rate))
    isk_tweet = isk_current[:-4]
    driver.quit()

    with open("isk.txt", "r+") as txt:
        old = txt.readlines()
        old = re.sub('[^.0-9]', '', str(old))
        txt.truncate(0)
        txt.close()

    with open("isk.txt", "r+") as txt:
        txt.write(isk_current)
        txt.close()

    current = float(isk_current)
    old = float(old)
    percentage = 100 * (current - old) / old
    list = []
    list.append(percentage)
    string = ''.join(str(e) for e in list)

    if "-" in string:
        well = '📉 ' + string[:5] + '%'
    else:
        well = '📈 ' + string[:4] + '%'

    isk_final = "🇮🇸 kr1 = ₺{} > {}\n".format(isk_tweet, well)
    return isk_final

while True:
    day_of_week = datetime.date.today().weekday()
    time = datetime.datetime.now().time()

    try:
        import time
        if day_of_week < 5 and (time > datetime.time(9,40) and time < datetime.time(18,15)):
            tweet()
            print("Done, sleeping for 15 minutes.")
            time.sleep(1800)
        else:
            print("hibernating..")
            time.sleep(5000)
    except ValueError:
        time.sleep(30)
        continue