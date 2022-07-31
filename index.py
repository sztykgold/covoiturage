import flask
import flask_login
import login_site
from flask import render_template, url_for

app = flask.Flask(__name__, static_folder='static', template_folder='templates')

#cette ligne ajoute les route definie dans login_site.py avec comme prefix de l'url 'users'
app.register_blueprint(login_site.login_site_blueprint, url_prefix='/users')

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app









@app.route('/')
@app.route('/home')
def home():
    '''
    if flask_login.current_user.is_authenticated :
        return 'Hello ' + flask_login.current_user.id
    else :
'''
    return render_template("index.html")

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    print("Host = " + str((HOST)) + " ; Port = " + str(PORT))
    login_site.init(app)
    app.run(HOST, PORT)
    