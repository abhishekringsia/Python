from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from com.agriold import data, dynamoClient

application = Flask(__name__)
cors = CORS(application)

header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''

application.add_url_rule('/', 'index', (lambda: header_text  + instructions))

application.add_url_rule('/<username>', 'hello', (lambda username:
                                                  header_text + username ))

@application.route('/tasks', methods=['GET'])
def get_tasks():
    return data.get_task()

@application.route('/task', methods=['POST'])
def add_task():
    req_data = request.get_json()
    dynamoClient.save_movie()
    return jsonify({"status": "success"})

@application.route('/postAd', methods=['POST'])
def post_ad():
    req_data = request.get_json()
    dynamoClient.save_post(req_data)
    return jsonify({"status": "success"})

@application.route('/ads', methods=['GET'])
def get_ad():
    req_data = request.get_json()
    data =  dynamoClient.get_posts()
    print("ads " , data)
    return jsonify(data)




if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
