from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# created by me
@app.route('/save')
def save_pallavi():
    return 'I am going to save values in it!';


# dynamic URL web service
@app.route('/user/<name>')
def show_user_profile(name):
    # show the user profile for that user
    return 'User %s' %name


@app.route('/post/<int:id>')
def show_post(id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % id


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()