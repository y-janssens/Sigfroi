import os
import subprocess
from backup.models import Snapshot
import smtplib
import ssl
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from backend.settings import SMTP, PORT, SENDER, PASSWORD


def backup_send_mail():
    # First, assess that there is existing backups and delete them to avoid duplicates.
    # The point here is since the database is saved into the content field of the object
    # Creating a new snapshot without deleting previous ones would lead to an exponential
    # Rise of the snapshot's weight. Making it at last impossible to process and send.
    # So there can't be more than one existing object at any given time.
    # The snapshot includes everything, including logs, and needs to be cleaned before
    # Any attempt to restore it to a fresh database. And is only saved to the model
    # To be downlodable directly from a view, avoiding S3 storage costs.

    snapshots = Snapshot.objects.all()
    if len(snapshots) == 0:
        pass
    else:
        for i in snapshots:
            i.delete()

    # Then perform an object creation
    snap = Snapshot.objects.create()

    # A bash script will dump the database, parse it into JSON and save it into a file
    subprocess.call([r'static/utils/parse.sh', f'{snap.uuid}'])

    # Open the file and save it's content to the object's content field
    f = open(rf"static/backups/{snap.uuid}.json", 'r')
    file_contents = f.read()
    snap.content = file_contents
    snap.save()
    f.close()

    # Add this file as an attachment before sending it to the administrator's email adress
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y")

    smtp = SMTP
    port = PORT
    sender = SENDER
    password = PASSWORD

    subject = f"Backup: {date_time}"
    receiver = 'marbrume.alias@gmail.com'
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject

    with open(rf"static/backups/{snap.uuid}.json", "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {snap.uuid}.json",
    )

    message.attach(part)
    text = message.as_string()

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp, port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, text)

    # Before removing the file
    os.remove(rf"static/backups/{snap.uuid}.json")
