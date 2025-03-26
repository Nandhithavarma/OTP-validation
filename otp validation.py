import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
num_users = int(input("How many users do you want enter: "))
for i in range (num_users) :
    
    otp = random.randint(1111,9999)
    body = f"OTP for verification is {otp}"

    msg = MIMEMultipart()
    msg["From"] = "nalivelanandhitha@gmail.com"
    msg["To"] = input("Enter your mail id: ")
    msg["Subject"] = "OTP For Validation"
    msg.attach(MIMEText(body,'plain'))

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("nalivelanandhitha@gmail.com","sone vaqe glmm ywzy")
    server.send_message(msg)
    server.quit()

    cotp = int(input("Enter OTP Recieved: "))
    if otp == cotp:
        print("OTP Verification Succes")
    else:
        print("Invalid OTP")
