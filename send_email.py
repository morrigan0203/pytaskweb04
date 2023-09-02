import yaml
import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

with open("./send_email.yaml") as f:
    params = yaml.safe_load(f)


class SendEmail:

    @staticmethod
    def create_message(from_addr, to_addr, report_name, subject, body):
        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Subject'] = subject
        with open(report_name, "rb") as f:
            part = MIMEApplication(f.read(), Name=basename(report_name))
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(report_name)
            msg.attach(part)
        msg.attach(MIMEText(body, 'plain'))
        return msg

    @staticmethod
    def send_message(from_addr, to_addr, my_pass, smpt_host, smpt_port, msg):
        server = smtplib.SMTP_SSL(smpt_host, smpt_port)
        server.login(from_addr, my_pass)
        text = msg.as_string()
        server.sendmail(from_addr, to_addr, text)
        server.quit()


if __name__ == "__main__":
    send_email = SendEmail()
    msg = send_email.create_message(params["from_addr"], params["to_addr"], params["report_name"],
                                    "Hello from python", "This is test message")
    send_email.send_message(params["from_addr"], params["to_addr"], params["my_pass"],
                            params["smtp_mail_host"], params["smtp_mail_port"], msg)
