from flask import Flask, render_template, request, send_file
#from flask import Flask
import cv2
import numpy as np
import os
import glob
import zipfile
#application = Flask(__name__, template_folder="templates")
application = Flask(__name__)
@application.route('/')
def home():
    return render_template('index.html')
    #return "hello world"
    
if __name__ == '__main__':
    application.run(debug=True)