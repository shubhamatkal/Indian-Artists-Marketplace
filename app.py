from flask import Flask , render_template
import os
from flask_bootstrap import Bootstrap5

#initializing flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASKKEY')
Bootstrap5(app)

#add a home page
@app.route('/')
def home_page():
    return render_template('home.html')














#end part of flask app
if __name__ == "__main__":
    app.run(debug=True, port = 5001)