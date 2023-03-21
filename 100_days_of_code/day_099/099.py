# Day 99: Scrape Replit Community Hub
import os
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import punctuation

import requests
import schedule
from bs4 import BeautifulSoup
from replit import db


def send_email(title, date, href) -> None:
    """Send email based on event title, date and URL."""
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
    msg['Subject'] = 'Latest Community Events'
    body = f'<a href="{href}">{title} {date}</a>'
    msg.attach(MIMEText(body, 'html'))
    s.send_message(msg)
    del msg


def get_new_events() -> None:
    """Extract new interesting events from the Replit Community Hub."""
    topics = [
        'python', 'education', 'coding', 'coder'
    ]

    keys = db.keys()
    # print(f'{keys = }')

    replit_url = 'https://replit.com/community-hub'
    response = requests.get(replit_url)
    html_page = BeautifulSoup(response.text, 'html.parser')
    events = html_page.find(
        'ul', {'class': 'css-fod6u7'}
    ).find_all('div', {'class': 'css-wi7uht'})

    for event in events:
        event_title = event.find('span', {'class': 'css-1p5fwdn'}).text
        event_date = event.find('span', {'class': 'css-chzm3s'}).text
        event_href = event.find('a').get('href')
        # remove any punctuation from each word
        words = [
            elem.translate(str.maketrans('', '', punctuation))
            for elem in event_title.split()
            if elem not in punctuation
        ]
        interested = False
        for word in words:
            if word.lower() in topics:
                interested = True
                break
        new_key = f'{event_title}_{event_date}'
        if interested and new_key not in keys:
            db[new_key] = {
                'event_title': event_title,
                'event_date': event_date,
                'event_href': event_href
            }
            send_email(event_title, event_date, event_href)
            # print(f'{event_title} added')


def main() -> None:
    # db.clear()
    # get_community_hub()
    schedule.every(5).hours.do(get_new_events())
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
