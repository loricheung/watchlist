#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: loricheung
from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello():
    return "Welcome to watchlist"


@app.route('/user/<name>')
def user_page(name):
    return f"Welcome, {name}!"


@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name='lori'))
    print(url_for('user_page', name='peter'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return "Test page"
