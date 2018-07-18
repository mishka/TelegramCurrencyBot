def main():
    import re, requests
    from bs4 import BeautifulSoup
    from datetime import datetime

    time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
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
    gbp_edit = re.sub('[^0-9,.]', '', str(gbp_rate))
    gbp_edit = gbp_edit[:-3]
    gbp_final = "£1 is ₺{} --> Pound Sterling\n".format(gbp_edit)

    print("Fetching eur data..")
    eur_url = requests.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=TRY", headers=headers)
    eur_data = eur_url.content
    eur_soup = BeautifulSoup(eur_data, 'html.parser')
    eur_rate = eur_soup.find('span', {'class' : 'uccResultAmount'})
    eur_edit = re.sub('[^0-9,.]', '', str(eur_rate))
    eur_edit = eur_edit[:-3]
    eur_final = "€1 is ₺{} --> Euro\n".format(eur_edit)

    print("Fetching usd data..")
    usd_url = requests.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=TRY", headers=headers)
    usd_data = usd_url.content
    usd_soup = BeautifulSoup(usd_data, 'html.parser')
    usd_rate = usd_soup.find('span', {'class' : 'uccResultAmount'})
    usd_edit = re.sub('[^0-9,.]', '', str(usd_rate))
    usd_edit = usd_edit[:-3]
    usd_final = "$1 is ₺{} --> United States Dollar\n".format(usd_edit)

    print("Fetching ils data..")
    ils_url = requests.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=ILS&To=TRY", headers=headers)
    ils_data = ils_url.content
    ils_soup = BeautifulSoup(ils_data, 'html.parser')
    ils_rate = ils_soup.find('span', {'class' : 'uccResultAmount'})
    ils_edit = re.sub('[^0-9,.]', '', str(ils_rate))
    ils_edit = ils_edit[:-3]
    ils_final = "₪1 is ₺{} --> Israeli New Shekel\n".format(ils_edit)

    print("Fetching rub data..")
    rub_url = requests.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=RUB&To=TRY", headers=headers)
    rub_data = rub_url.content
    rub_soup = BeautifulSoup(rub_data, 'html.parser')
    rub_rate = rub_soup.find('span', {'class' : 'uccResultAmount'})
    rub_edit = re.sub('[^0-9,.]', '', str(rub_rate))
    rub_edit = rub_edit[:-4]
    rub_final = "₽1 is ₺{} --> Russian Ruble\n".format(rub_edit)

    print("Fetching cny data..")
    cny_url = requests.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=CNY&To=TRY", headers=headers)
    cny_data = cny_url.content
    cny_soup = BeautifulSoup(cny_data, 'html.parser')
    cny_rate = cny_soup.find('span', {'class' : 'uccResultAmount'})
    cny_edit = re.sub('[^0-9,.]', '', str(cny_rate))
    cny_edit = cny_edit[:-4]
    cny_final = "¥1 is ₺{} --> Chinese Yuan \n".format(cny_edit)

    print("Fetching jpy data..")
    jpy_url = requests.get("https://www.xe.com/currencyconverter/convert/?Amount=1&From=JPY&To=TRY", headers=headers)
    jpy_data = jpy_url.content
    jpy_soup = BeautifulSoup(jpy_data, 'html.parser')
    jpy_rate = jpy_soup.find('span', {'class' : 'uccResultAmount'})
    jpy_edit = re.sub('[^0-9,.]', '', str(jpy_rate))
    jpy_edit = jpy_edit[:-4]
    jpy_final = "¥1 is ₺{} --> Japanese Yen\n".format(jpy_edit)

    import tweepy

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    api.update_status(status="{}\n\n{}{}{}{}{}{}{}".format(time, gbp_final, eur_final, usd_final, ils_final, rub_final, cny_final, jpy_final))
    print("Tweet sent!")

while True:
    import datetime
    day_of_week = datetime.date.today().weekday()
    time = datetime.datetime.now().time()

    if day_of_week < 5 and (time > datetime.time(9,40) and time < datetime.time(18,5)):
        main()
        import time
        time.sleep(900)
    else:
        print("hibernating..")
        import time
        time.sleep(900)
