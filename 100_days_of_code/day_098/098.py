# Day 98: Automate email sending
import os
import smtplib
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import choice


def get_local_quotes(quotes_file: str = 'tutorial/quotes.txt') -> list:
    """Return a list of quotes from a local text file."""
    with open(quotes_file, 'r') as file:
        quotes = eval(file.read())
    return quotes


def send_mail(quotes: list, mail_address: str, mail_pass: str) -> None:
    quote = choice(quotes)
    server = 'smtp.gmail.com'
    port = 587
    s = smtplib.SMTP(host=server, port=port)
    s.starttls()
    s.login(user=mail_address, password=mail_pass)

    msg = MIMEMultipart()
    msg['To'] = mail_address
    msg['From'] = mail_address
    msg['Subject'] = 'Daily quote'
    msg.attach(MIMEText(quote, 'html'))

    s.send_message(msg)
    del msg


def main() -> None:
    mail_address = os.getenv('MAIL_ADDRESS')
    mail_pass = os.getenv('MAIL_PASSWORD')
    quotes = get_local_quotes()
    # print(f'{choice(quotes) = }')
    # send_mail(
    #     quotes=quotes,
    #     mail_address=mail_address,
    #     mail_pass=mail_pass
    # )
    schedule.every(24).hours.do(
        lambda: send_mail(
            quotes=quotes,
            mail_address=mail_address,
            mail_pass=mail_pass
        )
    )
    while True:
        schedule.run_pending()
        # sleep reduces cpu usage
        time.sleep(1)


if __name__ == '__main__':
    main()
