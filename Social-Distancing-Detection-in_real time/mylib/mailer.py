import smtplib, ssl

class Mailer:

    """
    This script initiaties the email alert function.
    """
    def __init__(self):
        # Enter your email below. This email will be used to send alerts.
        # E.g., "email@gmail.com"
        self.EMAIL = "mps.tulasi@gmail.com"
        # Enter the email password below. Note that the password varies if you have secured
        # 2 step verification turned on. You can refer the links below and create an application specific password.
        # Google mail has a guide here: https://myaccount.google.com/lesssecureapps
        # For 2 step verified accounts: https://support.google.com/accounts/answer/185833
        # Example: aoiwhdoaldmwopau
        self.PASS = "PujithaSaiTulasi10"
        self.PORT = 465
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', self.PORT)

    def send(self, mail,serious):
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', self.PORT)
        self.server.login(self.EMAIL, self.PASS)
        # message to be sent
        SUBJECT = 'ALERT!'
        TEXT = f'Social distancing violations exceeded! and serious violations are {serious}'
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

        # sending the mail
        try:
            self.server.sendmail(self.EMAIL, mail, message)       
            self.server.quit()
            return 1
        except Exception:
             return 0
