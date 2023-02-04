from flask import Blueprint, render_template, request, redirect, url_for, flash

views = Blueprint('views', __name__)

@views.route('/')
def landing():
    return render_template('landing.html')

