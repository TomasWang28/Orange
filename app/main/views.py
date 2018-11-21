from flask import render_template
from . import main

@main.route('/main', methods=['POST', 'GET'])
def dashboard():
    return render_template("Dashboard.html")