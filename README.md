Birthday Wisher

This project automatically sends birthday wishes by checking birthdays stored in a CSV file.

Branches

1. master(whatsapp)
Uses:
- pandas
- pywhatkit
- datetime

Features:
- Reads birthdays from "birthdays.csv"
- Checks if today matches a birthday
- Chooses a random birthday message from the templates
- Sends the birthday wish through WhatsApp

2. smtp
Uses:
- pandas
- smtplib
- datetime

Features:
- Reads birthdays from "birthdays.csv"
- Checks if today matches a birthday
- Chooses a random birthday message from the templates
- Sends the birthday wish through email

Note : For the "smtp" branch, replace the "phone" column in "birthdays.csv" with an "email" column.
