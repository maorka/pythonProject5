import os
import smtplib
def MailAllertFunc(mail_allert):
 gmail_user = "#####@gmail.com"#Enter user mail
 gmail_pwd = "######"#Enter user Password
 TO = 'maor0525@gmail.com'
 SUBJECT = "PumbaParkingAllert"
 TEXT = "Parking spot number 1  available at Shalom-Haliechem 32,Keren Hchayedet"
 server = smtplib.SMTP('smtp.gmail.com', 587)
 server.ehlo()
 server.starttls()
 server.login(gmail_user, gmail_pwd)
 BODY = '\r\n'.join(['To: %s' % TO,
        'From: %s' % gmail_user,
        'Subject: %s' % SUBJECT,
        '', TEXT])
 server.sendmail(gmail_user, [TO], BODY)
 print ('email sent')

 return ()