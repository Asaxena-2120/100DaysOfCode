import smtplib

# Make it a very less secure account, go into the account and make it less secure
my_email = "asdfg@gmail.com"
password = "abcd1234()"

# To connect to gmail server
with smtplib.SMTP("smtp.gmail.com") as connection:
    # Transport layer security: way of securing our connection to our email server
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="asdfg@yahoo.com",
                        msg="Subject:Hello\n\nThis is the body of my email.")

