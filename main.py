import pywhatkit,random
import pandas as pd
import  datetime as dt

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
        phone = person["phone"]
        pywhatkit.sendwhatmsg(f"+91{phone}",f"Happy Birthday!!!\n\n{content}",8,00)