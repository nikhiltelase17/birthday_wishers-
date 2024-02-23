import pandas
import datetime
import random
import smtplib

# getting current month and bay
now = datetime.datetime.now()
now_month = now.month
now_day = now.day

# reading birthday csv
birthday_data = pandas.read_csv("birthdays.csv")
birthday_dict = birthday_data.to_dict(orient="records")

# checking birthdays
for person in birthday_dict:
    if person['month'] == now_month and person["day"] == now_day:
        name = person["name"]
        email = person["email"]
        print("name: ", name)
        print("email: ", email)

        # picking random letter from letter_templates
        random_num = random.randint(1, 3)
        with open(f"letter_templates/letter_{random_num}.txt") as letter_file:
            letter = letter_file.read()

        # creating birthday letter for birthday person
        birthday_letter = letter.replace("[NAME]", f"{name}")

        # sending birthday letter
        my_email = "nikhiltelase@gmail.com"
        password = "kpszkfnemcimpssz"
        to_mail = email
        message = f"Subject: Happy Birthday \n\n{birthday_letter}"

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()  # seure
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=[to_mail],
                                msg=message)
        print("I send a birthday letter")
