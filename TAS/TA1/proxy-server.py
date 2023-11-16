from flask import Flask, jsonify, Response, request, send_from_directory, render_template, redirect
from flask_cors import CORS
import requests
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

app = Flask(__name__)
# Enable CORS so that we can make cross origin calls from server
CORS(app)

# Create target_url variable and set it to login page of a website
target_url = "https://www.netflix.com/Login"

@app.route('/', methods=['GET', 'POST'])
def serve_index():
    return render_template('index.html')

# Create a /proxy route
@app.route('/proxy')
# Define proxy() function
def proxy():
    # Use request.get() to get the login page from target_url and save it in response
    response = requests.get(target_url)
    # return Response(response.text, status=response.status_code, content_type=response.headers['content-type'])
    return Response(response.text, status=response.status_code, content_type=response.headers['content-type'])
    
if __name__ == '__main__':
    app.run(port=5000)
