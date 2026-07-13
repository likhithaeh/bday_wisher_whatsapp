import smtplib,random
import datetime as dt
import pandas as pd

today = (dt.datetime.now().month,dt.datetime.now().day)
data_row = pd.read_csv("birthdays.csv")
name = data_row["name"]
month = data_row["month"]
day = data_row["day"]
bday_dict = {(row.month,row.day):row for (_,row) in data_row.iterrows()}
if today in bday_dict:
    letter = random.randint(1,3)
    letter_name = f"letter_templates/letter_{letter}.txt"
    with open(letter_name,"r") as letter:
        content = letter.read()
        person = bday_dict[today]
        content = content.replace('[NAME]',person["name"])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                 connection.starttls()
                 connection.login(user=my_email, password=password)
                 connection.sendmail(from_addr=my_email, to_addrs=person["email"], msg=f"Subject:Happy Birthday!!\n\n{content}")





