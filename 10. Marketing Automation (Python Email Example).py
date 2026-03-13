import smtplib

def send_newsletter(email):

    message = """
Subject: New Arrivals

Discover our newest minimalist dresses.
"""

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()

    server.login("your@email.com","password")

    server.sendmail("store@email.com",email,message)