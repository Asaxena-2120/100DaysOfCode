# import smtplib
#
# # Make it a very less secure account, go into the account and make it less secure
# my_email = "asdfg@gmail.com"
# password = "abcd1234()"
#
# # To connect to gmail server
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # Transport layer security: way of securing our connection to our email server
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="asdfg@yahoo.com",
#                         msg="Subject:Hello\n\nThis is the body of my email.")

import datetime as dt
import random
import smtplib

# obtain current day of the week
current_day = dt.datetime.now().weekday()
if current_day == 2:
    # Open quotes.txt file

    with open("quotes.txt","r") as file:
        content = file.readlines()
        # Use the random module to pick a random quote from your list of quotes
        random_quote = random.choice(content)


    #  Use the smtplib to send the email to yourself
    # Make it a very less secure account, go into the account and make it less secure
    my_email = "asdfg@gmail.com"
    password = "abcd1234()"

    # To connect to gmail server
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Transport layer security: way of securing our connection to our email server
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="asdfg@yahoo.com",
                            msg=f"Subject:Hello\n\n{random_quote}")
