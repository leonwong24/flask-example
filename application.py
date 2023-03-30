from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello_world():
    return 'Hello World'
    return 'Second_hello_world'
    
if __name__ == '__main__':
    application.run(debug=True)