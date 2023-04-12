import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Ion Crianga'
email['to'] = 'pmr-photo@mail.ru'
email['subject'] = 'Buna ziua!'

email.set_content('Python the best')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('pmr-photo@gmail.com', 'writepassword')
    smtp.send_message(email)
    print('good job!')
