#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   request_object.py
@Time    :   2020/4/1318:29
@Author  :   jiangheng
@Description    :   None
"""

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password.'
    return render_template('login.html', error=error)
