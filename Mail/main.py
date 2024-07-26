import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import datetime as dt

def create_mail():
    
    data = {
        'Date': [dt.datetime.today()],
        'Sales': [1000],
        'New Costumers': [10]}
    
    df = pd.DataFrame(data)
    
    return df.to_html()

def send_email(from_email, from_password, subject, body, to_email):
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'html'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        txt = msg.as_string()
        server.sendmail(from_email, to_email, txt)
        server.quit()
        print('Mail gönderildi.')
        
    except Exception as e:
        print('Mail gönderilemedi:', str(e))
        
def main():
    report = create_mail()
    from_email= str(input('Enter your mail adress. ')).strip()
    from_password = str(input('Enter your password. ')).strip()
    subject = str(input('Subject: ')).strip()
    to_email = []
    while True:
        email = str(input("Enter the target email adress ('q' to quit): ")).strip()
        if email.upper().strip() == 'Q':
            break
        to_email.append(email)
    
    for email in to_email:
        send_email(from_email, from_password, subject, report, email)
        
   
if __name__ == '__main__':
    main()