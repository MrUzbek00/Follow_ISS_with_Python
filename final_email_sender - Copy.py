import smtplib
import datetime as dt 
class Email_Notify:
    def __init__(self, message) -> None:
        self.my_email="" #Email address to send message
        self.my_password = "" #Email SMTP application password
        self.my_client = "" #To whom you would like to send an email
        self.message = message
    
    def send_email(self):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.my_password)
            connection.sendmail(from_addr=self.my_email, to_addrs=self.my_client, msg=self.message)


