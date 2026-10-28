import smtplib
import datetime as dt
import random
import pandas as pd
import os

now = dt.datetime.now()
year_now = now.year
month_now = now.month
day_now = now.day
day_of_week = now.weekday()

letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
chosen_letter = random.choice(letters)



MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

birthdays_df = pd.read_csv("birthdays.csv")

for row in birthdays_df.itertuples():
    if row[4] == month_now and row[5] == day_now:
        with open(f"{chosen_letter}", "r") as f:
            letter = f.read()
            named_letter = letter.replace("[NAME]", f"{row[1]}")
            print(named_letter)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.set_debuglevel(1)

            print("Connected to SMTP server")
            connection.ehlo()
            print("EHLO successful")
           connection.starttls()
           connection.login(user=MY_EMAIL, password=MY_PASSWORD)
           connection.sendmail(from_addr=MY_EMAIL, to_addrs=f"{row[2]}", msg="Subject:Happy Birthday!\n\n"
                                                                                         f"{named_letter}\n\n")
