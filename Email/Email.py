import smtplib
from email.message import EmailMessage

def send_mail(sender, app_password, receiver, subject, body):
    
    msg = EmailMessage()
    
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    
    msg.set_content(body)
    
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    
    smtp.login(sender, app_password)
    
    smtp.send_message(msg)   
    
    smtp.quit()
    
def main():
    sender_email = "adityatest0710@gmail.com"
    
    app_password = "ptcs rues gxst gyto"
    
    receiver_email = "adityasanap2001@gmail.com"
    
    subject = "Test Mail from python script"
    
    body = """Jay Ganesh,
    This is a test email sent using Python script
    regards,
    Aditya Sanap
    """
    
    send_mail(sender_email, app_password, receiver_email, subject, body)
    
    print("Mail sent successfully")
        
if __name__ == "__main__":
    main()    