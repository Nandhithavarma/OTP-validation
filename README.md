OTP Email Verification System 📧🔐
This Python script is designed to generate and send a One Time Password (OTP) via email to multiple users, and then verify the OTP entered by the user. It utilizes the smtplib library to send emails via Gmail’s SMTP server and performs basic input validation and error handling.

Key Features 🔑:
Multi-User Support 👥
The script allows sending OTPs to multiple users by taking the number of users as input. It will then loop to send OTPs to each user's email address.

OTP Generation 🔢
The script generates a 4-digit random OTP (One Time Password) for each user, which is sent to their email address for verification.

Email Sending via Gmail SMTP 📧
Utilizes Gmail’s SMTP server (smtp.gmail.com on port 587) to send OTP emails. This allows you to send secure and fast OTP emails to users.

Email Validation ✔️
Ensures that the email address provided by the user is in the correct format. If an invalid email is entered, the script skips sending the OTP for that user.

Secure Email Login 🔑
The script uses an environment variable (EMAIL_PASSWORD) to store the email password securely, reducing the risk of exposing sensitive information. It uses the Gmail App Password feature to authenticate and send emails.

OTP Verification 🔍
After sending the OTP to the user, the script prompts the user to enter the OTP they received. It then compares the entered OTP with the generated one and provides feedback on whether the verification was successful or not.

Error Handling 🚨
The script includes basic error handling to catch issues like incorrect email formats or failures in sending OTPs. If something goes wrong while sending the email, an error message is displayed.

Efficient SMTP Usage ⚡
The script opens a single SMTP connection at the beginning and reuses it to send OTPs to all users, making it more efficient.
