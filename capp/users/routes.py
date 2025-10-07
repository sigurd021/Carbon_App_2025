from flask import render_template, Blueprint, redirect, url_for, flash
from capp.users.forms import RegistrationForm, LoginForm

users=Blueprint('users',__name__)

@users.route('/register', methods=['GET','POST'])
def register():
  form=RegistrationForm()
  if form.validate_on_submit():
    flash('Your account has been created! You can now log in')
    return redirect(url_for('home.home_home'))
  return render_template('users/register.html', title='register', form=form)

@users.route('/login', methods=['GET','POST'])
def login():
  form=LoginForm()
  if form.validate_on_submit():
    flash('You have been logged in!')
    return redirect(url_for('home.home_home'))
  return render_template('users/login.html', title='login', form=form)