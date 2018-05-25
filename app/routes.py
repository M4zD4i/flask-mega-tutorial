#-*- encoding: utf-8 -*-

from flask import render_template
from app import myapp

@myapp.route('/')
@myapp.route('/index')
def index():
    user = { 'name' : 'M4zD4i' }
    messages = [
        {
            'user': {'name': 'Alice'},
            'text': 'Wow!'
        },
        {
            'user': {'name': 'Bob'},
            'text': 'Cool!'
        }
    ]
    return render_template('index.html', title = 'Chapter 2', user = user, messages=messages)