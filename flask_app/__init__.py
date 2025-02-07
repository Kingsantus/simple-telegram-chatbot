from flask import Flask

# instantiate the app
def create_app():
    app = Flask(__name__)
    return app