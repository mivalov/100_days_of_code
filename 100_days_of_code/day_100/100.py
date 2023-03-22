# Day 100: Product Price Scraper
import locale
import os
import re
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests
import schedule
from bs4 import BeautifulSoup
from replit import db


def currency_to_float(price: str) -> float:
    """Convert currency string to a float number."""
    decimal_point = locale.localeconv()['decimal_point']
    clean_price = re.sub(r'[^0-9' + decimal_point + r']+', '', str(price))
    return float(clean_price)


def add_to_db() -> None:
    """Add product to the database."""
    url = input('Product URL: ')
    try:
        desired_price = float(input('Desired price: '))
    except ValueError:
        print('Please enter your price as float.')
    else:
        version = str(int(time.time()))
        db[version] = {
            'url': url,
            'price': None,
            'desired_price': desired_price
        }


def send_mail(url, price, desired_price) -> None:
    """Send email based on URL, price and desired price for a given product."""
    email_address = os.getenv('MAIL_ADDRESS')
    email_pass = os.getenv('MAIL_PASSWORD')
    server = 'smtp.gmail.com'
    port = 587
    s = smtplib.SMTP(host=server, port=port)
    s.starttls()
    s.login(user=email_address, password=email_pass)

    msg = MIMEMultipart()
    msg['To'] = email_address
    msg['From'] = email_address
    msg['Subject'] = 'Product is at a lower price!'
    body = f'<p><a href="{url}">This article</a> currently costs {price}, ' \
           f'which is below your budget ({desired_price})</p>'
    msg.attach(MIMEText(body, 'html'))
    s.send_message(msg)
    del msg


def price_update() -> None:
    keys = db.keys()
    for key in keys:
        url = db[key].get('url')
        price = db[key].get('price')
        desired_price = db[key].get('desired_price')
        response = requests.get(url).text
        html = BeautifulSoup(response, 'html.parser')
        current_price = html.find_all('span', {'class': 'price'})
        current_price = currency_to_float(current_price[0].text)
        if price != current_price:
            db[key]['price'] = current_price
        if current_price <= desired_price:
            print('Lower price!')
            send_mail(
                url=url,
                price=current_price,
                desired_price=desired_price
            )


def main() -> None:
    add_to_db()
    schedule.every(1).day.do(price_update())
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
