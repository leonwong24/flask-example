from flask import Flask, render_template, request, send_file
import cv2
import numpy as np
import os
import glob
import zipfile
application = Flask(__name__, template_folder="templates")

@application.route('/')
def home():
    return render_template('index.html')

    
if __name__ == '__main__':
    application.run(debug=True)