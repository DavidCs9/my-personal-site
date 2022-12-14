import os
import smtplib
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
# EMAIL = "decsiqueiros198@gmail.com"
# PSW = os.environ['PSW']

application = app = Flask(__name__)


# def send_mail(name, email, subject, message):
#    with smtplib.SMTP("smtp.gmail.com") as connection:
#        connection.starttls()
#        connection.login(user=EMAIL, password=PSW)
#        connection.sendmail(
#            from_addr=EMAIL,
#            to_addrs="davidcastrosi@hotmail.com",
#            msg=f"Subject:{subject}\n\nMessage: {message}\nName: {name} Email: {email}"
#        )


@app.route("/", methods=['GET', 'POST'])
def home():
    # name = request.form.get('name')
    # email = request.form.get('email')
    # subject = request.form.get('subject')
    # message = request.form.get('message')

    # if request.method == 'POST':
    #    send_mail(name, email, subject, message)
    #    return render_template("email.html")

    return render_template("index.html")


# @app.route("/email", methods=['GET'])
# def email():
#    return render_template("email.html")


if __name__ == "__main__":
    application.run(debug=True)
