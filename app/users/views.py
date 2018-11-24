from flask import render_template
from . import users

@users.route('/users', methods=['POST', 'GET'])
def userviews():
    return render_template('users/users.html')