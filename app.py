from flask import Flask, render_template

app = Flask(__name__)

from routes import *

# run Flask app
if __name__ == "__main__":
    app.run()