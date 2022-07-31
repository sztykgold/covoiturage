import flask_login

# Our mock database.
users = {'foo@bar.tld': {'password': 'secret'}}
login_manager = flask_login.LoginManager()

class User(flask_login.UserMixin):
    pass

def init(app):
    app.secret_key = 'super secret string'  # Change this!    
    login_manager.init_app(app)


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Merci de bien vouloir vous authentifier !', 401