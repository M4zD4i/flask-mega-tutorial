#-*- encoding: utf-8 -*-

from flask import render_template, flash, redirect, url_for
from app import myapp
from app.forms import LoginForm

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
    return render_template('index.html', title = 'Chapter 3', user = user, messages=messages)

@myapp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title = 'Log in, please..', form=form)