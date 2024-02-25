import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import matplotlib.pyplot as plt
import numpy as np

def send_email(sender_email, sender_password, recipient_email, subject, message, attachment_path):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the message body
    msg.attach(MIMEText(message, 'plain'))

    # Attach the chart image
    with open(attachment_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {attachment_path}",
    )
    msg.attach(part)

    # Connect to the SMTP server and send the message
    smtp_server = 'smtp.office365.com'
    smtp_port = 587

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())

    print("Email sent successfully!")

# Generate some sample data and plot a chart
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

# Save the chart image to a file
chart_image_path = 'chart.png'
plt.savefig(chart_image_path)

# Send the email with the chart attached

recipient_email = 'shayan5mouktar@gmail.com'
sender_email = 'farihy@outlook.fr'
sender_password = 'jtdgdt78'

subject = 'Chart Attached'
message = 'Please find the chart attached.'
def send(message,destinator, chart, object):
    send_email(sender_email, sender_password, destinator, object, message,chart)


