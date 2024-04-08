from flask import Flask, jsonify
import os
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return 'Helloooooooooooo+'


@app.route('/about')
def about():
    return "We accept the fight"


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
