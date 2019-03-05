import os, csv, random, tweepy
import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio
from plotly.offline import plot
from datetime import datetime
from PIL import Image
from math import ceil, floor

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

def today():
    return str(datetime.today().strftime('%d-%m-%Y'))

def random_colour():
    color_hex = [""+''.join([random.choice('0123456789ABCDEF') for x in range(6)])for i in range(1)]
    return '#' + str(color_hex)[2:-2]

def reset_csv():
    with open('chart.csv', 'w') as f:
        fwrite = csv.writer(f)
        fwrite.writerow(['TIME', 'GBP', 'EUR', 'USD', 'CAD', 'QAR', 'RUB', 'CNY', 'JPY', 'KRW'])
        f.close()
    return print('Created a new csv file!')

def tweet():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    imgfile = "{}/daily_charts/{}.png".format(os.getcwd(), today())
    api.update_with_media(imgfile, status=f"{today()}")
    print("Tweet sent!")

def generate_images():
    df = pd.read_csv('chart.csv')
    currencies = ["GBP", "EUR", "USD", "CAD", "QAR", "RUB", "CNY", "JPY", "KRW"]

    for currency in currencies:
        print(f"Generating {currency}")
        data = go.Scatter(
            x = df['TIME'],
            y = df[currency],
            line = dict(color = random_colour()))

        fig = dict(data = [data], layout = dict(title = f"{currency}"))
        pio.write_image(fig, f'generated_pics/{currency}.png', width=1000, height=550, scale=5)

def generate_chart():
    images = ["generated_pics/GBP.png", "generated_pics/EUR.png", "generated_pics/USD.png",
            "generated_pics/CAD.png", "generated_pics/QAR.png", "generated_pics/RUB.png",
            "generated_pics/CNY.png", "generated_pics/JPY.png", "generated_pics/KRW.png"]

    frame_width = 7680
    images_per_row = 3
    padding = 0

    img_width, img_height = Image.open(images[0]).size
    sf = (frame_width - (images_per_row - 1) * padding) / (images_per_row * img_width)
    scaled_img_width = ceil(img_width * sf)
    scaled_img_height = ceil(img_height * sf)

    number_of_rows = ceil(len(images) / images_per_row)
    frame_height = ceil(sf * img_height * number_of_rows) 

    new_im = Image.new('RGB', (frame_width, frame_height))
    i, j = 0, 0

    for num, im in enumerate(images):
        if num % images_per_row == 0:
            i = 0
        im = Image.open(im)
        im.thumbnail((scaled_img_width, scaled_img_height), Image.ANTIALIAS)
        y_cord = (j // images_per_row) * scaled_img_height
        new_im.paste(im, (i, y_cord))
        i = (i + scaled_img_width) + padding
        j += 1

    new_im.save(f"daily_charts/{today()}.png", "PNG", quality=100)
    return print('Generated the chart!')

generate_images()
generate_chart()
reset_csv()
tweet()