import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from decouple import config


def send_email(to_email, cc_email, body, extra_info, subject):
    # Set up the email server and credentials.
    smtp_server = config('SMTP_SERVER')
    smtp_port = 587
    smtp_username = config('SMTP_USERNAME')
    smtp_password = config('SMTP_PASSWORD')

    # Create the email message.
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Cc'] = cc_email
    msg['Subject'] = subject

    # Attach the extra information to the email body.
    body += f"\n\nExtra Information: {extra_info}"

    msg.attach(MIMEText(body, 'plain'))

    # Send the email.
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, [to_email, cc_email], msg.as_string())
        return True
    except Exception as e:
        return str(e)

