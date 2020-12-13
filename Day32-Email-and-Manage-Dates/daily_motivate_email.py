# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# print(year)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15)
# print(date_of_birth)

import smtplib
import datetime as dt
import random

MY_EMAIL = "myemail@gmail.com"
MY_PASSWORD = "mypass"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}".encode(encoding="utf8")
        )
