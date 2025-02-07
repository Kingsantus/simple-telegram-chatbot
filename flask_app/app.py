from flask import request
from . import create_app
from .chatbot import get_bot_response

app = create_app()

# creating / route
@app.route("/")
def index():
    return "Hello World"

# creating /get route
@app.route("/get")
def get_response():
    # get message from request coming to the url
    user_text = request.args.get("msg")
    # throw error if no request
    if not user_text:
        return "Message is required!", 400
    # return an Ai response
    return get_bot_response(user_text)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
