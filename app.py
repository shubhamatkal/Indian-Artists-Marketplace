from flask import Flask
import os

#initializing flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASKKEY')














#end part of flask app
if __name__ == "__main__":
    app.run(debug=True, port = 5001)