# -*- coding: utf-8 -*-
def main():
    import re, requests
    from bs4 import BeautifulSoup
    from datetime import datetime

    time = datetime.now().strftime('%H:%M')
    print(time + "\n")
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

    print("Fetching gbp data..")
    gbp_url = requests.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=GBP&To=TRY", headers=headers)
    gbp_data = gbp_url.content
    gbp_soup = BeautifulSoup(gbp_data, 'html.parser')
    gbp_rate = gbp_soup.find('span', {'class' : 'uccResultAmount'})
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

    print("Fetching eur data..")
    eur_url = requests.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=TRY", headers=headers)
    eur_data = eur_url.content
    eur_soup = BeautifulSoup(eur_data, 'html.parser')
    eur_rate = eur_soup.find('span', {'class' : 'uccResultAmount'})
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

    print("Fetching usd data..")
    usd_url = requests.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=TRY", headers=headers)
    usd_data = usd_url.content
    usd_soup = BeautifulSoup(usd_data, 'html.parser')
    usd_rate = usd_soup.find('span', {'class' : 'uccResultAmount'})
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

    print("Fetching ils data..")
    ils_url = requests.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=ILS&To=TRY", headers=headers)
    ils_data = ils_url.content
    ils_soup = BeautifulSoup(ils_data, 'html.parser')
    ils_rate = ils_soup.find('span', {'class' : 'uccResultAmount'})
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

    print("Fetching rub data..")
    rub_url = requests.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=RUB&To=TRY", headers=headers)
    rub_data = rub_url.content
    rub_soup = BeautifulSoup(rub_data, 'html.parser')
    rub_rate = rub_soup.find('span', {'class' : 'uccResultAmount'})
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

    rub_final = "🇷🇺 ₽1 = ₺{} > {}\n".format(rub_tweet, well)

    print("Fetching cny data..")
    cny_url = requests.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=CNY&To=TRY", headers=headers)
    cny_data = cny_url.content
    cny_soup = BeautifulSoup(cny_data, 'html.parser')
    cny_rate = cny_soup.find('span', {'class' : 'uccResultAmount'})
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

    print("Fetching jpy data..")
    jpy_url = requests.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=JPY&To=TRY", headers=headers)
    jpy_data = jpy_url.content
    jpy_soup = BeautifulSoup(jpy_data, 'html.parser')
    jpy_rate = jpy_soup.find('span', {'class' : 'uccResultAmount'})
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

    print("Fetching krw data..")
    krw_url = requests.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=KRW&To=TRY", headers=headers)
    krw_data = krw_url.content
    krw_soup = BeautifulSoup(krw_data, 'html.parser')
    krw_rate = krw_soup.find('span', {'class' : 'uccResultAmount'})
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

    print("Fetching isk data..")
    isk_url = requests.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=ISK&To=TRY", headers=headers)
    isk_data = isk_url.content
    isk_soup = BeautifulSoup(isk_data, 'html.parser')
    isk_rate = isk_soup.find('span', {'class' : 'uccResultAmount'})
    isk_current = re.sub('[^0-9,.]', '', str(isk_rate))
    isk_tweet = isk_current[:-4]

    with open("isk.txt", "r+") as txt:
        old = txt.readlines()
        old = re.sub('[^.0-9]', '', str(old))
        txt.truncate(0)
        txt.close()

    with open("isk.txt", "r+") as txt:
        txt.write(isk_current)
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

    isk_final = "🇮🇸 kr1 = ₺{} > {}\n".format(isk_tweet, well)

    import tweepy

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    print("{}\n\n{}{}{}{}{}{}{}{}{}".format(time, gbp_final, eur_final, usd_final, ils_final, cny_final, rub_final, isk_final, jpy_final, krw_final))

    api.update_status(status="{}\n\n{}{}{}{}{}{}{}{}{}".format(time, gbp_final, eur_final, usd_final, ils_final, cny_final, rub_final, isk_final, jpy_final, krw_final))
    print("Tweet sent!")

while True:
    try:
        import datetime
        day_of_week = datetime.date.today().weekday()
        time = datetime.datetime.now().time()

        if day_of_week < 5 and (time > datetime.time(9,40) and time < datetime.time(18,15)):
            main()
            print("Done, sleeping for 15 minutes.")
            import time
            time.sleep(900)
        else:
            print("hibernating..")
            import time
            time.sleep(900)
    except ValueError:
        continue
