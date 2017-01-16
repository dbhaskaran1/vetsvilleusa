import os
from flask import Flask, render_template, send_from_directory, request
import smtplib

app = Flask(__name__, static_url_path="/static", static_folder="static")

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = False
MAIL_USE_SSL = True

@app.route("/", methods=['GET', 'POST'])
@app.route("/index.html", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.form['message'] + ' from [' + request.form['phoneNo'] + request.form['emailID'] + request.form['fullName'] + ']'
        msg = "Message [{}] from {}. Email id {} and phone no {}.".format(request.form['message'], request.form['fullName'], request.form['emailID'], request.form['phoneNo'])
        send_email(msg=msg)
        return render_template('index.html')
    else:
        return render_template('index.html')

@app.route("/faqs.html", methods=['GET','POST'])
def details():
    return render_template('faqs.html')

@app.route('/robots.txt')
@app.route('/sitemap.xml')
@app.route('/rss.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


def send_email(msg='msg', recipient='vetsvilleusa@gmail.com', sender='somesender@gmail.com'):
    sender='vetsvilleusa@gmail.com'
    recipient=['vetsvilleusa@gmail.com', 'abc.keith48@gmail.com']
    server = smtplib.SMTP('smtp.gmail.com',587) #port 465 or 587
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.sendmail('vetsvilleusa@gmail.com',recipient,msg)
    server.close()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
