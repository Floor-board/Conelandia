from flask import Flask, request, render_template, flash, request
from markupsafe import Markup

import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/page2')
def NTPY():
    return render_template('page2.html')

@app.route('/page3')
def NTCPC():
    return render_template('page3.html')

@app.route('/page4')
def IINTPY():
    return render_template('page4.html')
    
@app.route('/page5')
def TEOTB():
    return render_template('page5.html')

if __name__=="__main__":
    app.run(debug=False)
