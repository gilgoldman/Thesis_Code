from datetime import datetime
from flask import Flask, render_template # Web Framework
import numpy as np # For fancy math
import os
from pathlib import Path
import sqlite3 # Database
import time # guess

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/on')
def led_on():
    text_test = Path("/home/pi/Thesis_Code/Text_Signal.txt")
    if text_test.is_file():
        try:
            os.remove("Test_Signal.txt")
        except OSError:
	    pass
    else:
	text_instance = open("Test_Signal.txt", "w")
	text_instance.write("On")
	text_instance.close()

    return "Are you feeling it now Mr. Krabs?"


if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')

