import flask_login
import flask
from flask import Blueprint
from user import *

login_site_blueprint = Blueprint('login_site', __name__)

# Our mock database.
#users = {'foo@bar.tld': {'password': 'secret'}}
users = {}

login_manager = flask_login.LoginManager()

def init(app):
    app.secret_key = 'super secret string'  # Change this!    
    login_manager.init_app(app)

@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    return users[email]
    #user = User(user_email=email)
    #return user

@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return
    return users[email]
    '''
    user = User(user_email=email)
    return user
    '''


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Merci de bien vouloir vous authentifier !', 401

@login_site_blueprint.route('/record', methods=['GET', 'POST'])
def record():
    if flask.request.method == 'GET':
        return '''
               <form action='record' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''
    email = flask.request.form['email']
    if email in users :
        return 'email déjà existant'
    
    if len(flask.request.form['password']) < 3 :
        return 'mot de passe trop court !'

    users[email] = BerthelotUser(user_email = email, password = flask.request.form['password']) #{'password':flask.request.form['password']}
    return flask.redirect(flask.url_for('login_site.login'))

@login_site_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''
    email = flask.request.form['email']
    if email in users and flask.request.form['password'] == users[email].password:
        flask_login.login_user(users[email])
        return flask.redirect(flask.url_for('login_site.protected'))

    return 'Bad login'

@login_site_blueprint.route('/protected')
@flask_login.login_required
def protected():
    return flask.redirect(flask.url_for('home'))

@login_site_blueprint.route('/logout')
def logout():
    flask_login.logout_user()
    return flask.redirect(flask.url_for('home'))

@login_site_blueprint.route('/fill_user_data', methods=['GET', 'POST'])
@flask_login.login_required
def fill_user_data():
    if flask.request.method == 'POST':
        user = user_loader(flask_login.current_user.id)
        user.phone = flask.request.form['phone']
        user.zipcode = flask.request.form['zipcode']
        user.city = flask.request.form['city']
        
        for wd in WorkingDay :
            requestKey = 'A' + wd.name + 'In'
            user.AWeek._data[wd.name][0] = WorkingHour[flask.request.form[requestKey]]
            user.AWeek._data[wd.name][1] = WorkingHour[flask.request.form['A' + wd.name + 'Out']]
            user.BWeek._data[wd.name][0] = WorkingHour[flask.request.form['B' + wd.name + 'In']]
            user.BWeek._data[wd.name][1] = WorkingHour[flask.request.form['B' + wd.name + 'Out']]

        #user.record() TODO
        return flask.redirect(flask.url_for('home'))
    else:
        return flask.render_template("fill_user_data.html")

