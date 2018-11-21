from flask import render_template,request,redirect,flash,session
from ..modules import User
from . import auth
from .. import login_manager
from flask_login import login_user, logout_user, login_required


@auth.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        _username = request.form['username']
        _password = request.form['password']
        print (_username, _password)
        user = User.query.filter_by(user_name = _username).first()

        if user is not None and user.verify_password(_password):
            login_user(user)
            session['username'] = user.user_name
            session['role_id'] = user.role_id
            print(session)
            return redirect('/main')
            # return redirect(request.args.get('next') or '/info')

        flash('Invalid username or password.')
        return render_template('login.html')


@login_manager.unauthorized_handler
def unauthorized_handler():
    # return 'Unauthorized: You have no access to this page.'
    return render_template('Errors/unauthorized.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

@auth.route('/main')
@login_required
def dashboard():
    return render_template('Dashboard.html', user_name = session.get('username'))




