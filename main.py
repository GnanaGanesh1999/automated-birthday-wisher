import smtplib
import pandas as pd
import datetime as dt
import random

# Constants
SMTP_SERVER = "smtp.mail.yahoo.com"
MY_EMAIL = "gnanaganesh1999@yahoo.com"
PASSWORD = "fzpwrezdxcjxzmns"
DEFAULT_SUBJECT = "Happy Birthday! ,"
SENDER = "Gnana Ganesh S"

# Collect today date
today_date = dt.datetime.today().date()
month = today_date.month
day = today_date.day

# Collect and Check Birthday
bd_data = pd.read_csv("birthday/birthdays.csv")
for bd in bd_data.iterrows():
    # if today is a birthday
    if bd[1].month == month and bd[1].day == day:
        name = bd[1][0]
        to_email = bd[1].email
        # Collect a random letter
        letter_number = random.randint(1, 3)
        with open(f"letters/letter_{letter_number}.txt") as letter_file:
            body_of_letter = letter_file.read()
            body_of_letter = body_of_letter.replace("[NAME]", name)
            body_of_letter = body_of_letter.replace("[S_NAME]", SENDER)

        # Send mail
        DEFAULT_SUBJECT += name
        with smtplib.SMTP(SMTP_SERVER) as connection:
            connection.starttls()
            connection.login(
                user=MY_EMAIL,
                password=PASSWORD
            )
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=to_email,
                msg=f"Subject: {DEFAULT_SUBJECT}\n\n{body_of_letter}"
            )
