##################### Extra Hard Starting Project ######################
# Imports
import pandas
import smtplib
import datetime as dtm

# Variables
cont = True
name = [];email = [];year = [];month = [];day = []
#Read letter
with open("letter_templates/letter_1.txt") as letter:
    letter_msg=letter.read()

# Enter Info and Generate the data file
while cont:
    name.append(input("Name of the person: "))
    email.append(input("Email of the person: "))
    year.append(input("Year of the person: "))
    month.append(input("Month of the person: "))
    day.append(input("Day of the person: "))
    s = input("Do you want to Enter more:(Y,N): ").lower()
    if s == 'y':
        continue
    elif s == 'n':
        break

file1 = {"name": [n for n in name], "email": [n for n in email], "year": [n for n in year], "month": [n for n in month],
         "day": [n for n in day]}
file2 = pandas.DataFrame(file1)
file2.to_csv("birthdays.csv", index=False)
# Match and Read
try:
    data = pandas.read_csv("birthdays.csv",index_col=False)
    data = data.to_dict()
except:
    print("Birthday File is missing please Enter data")

for n in data["month"]:
    month = dtm.datetime.now().month
    day = dtm.datetime.now().day
    if data["month"][n] == month and data["day"][n]==day:
        letter_msg=letter_msg.replace("[NAME]",data["name"][n])
        connection = smtplib.SMTP("smtp.example.com", port=587)
        connection.starttls()
        connection.login(user="example@example.com", password="examplepassword")
        connection.sendmail(from_addr="example@example.com", to_addrs=data["email"][n],msg=f"Subject:Happy Birthday\n\n {letter_msg}")
        connection.close()


