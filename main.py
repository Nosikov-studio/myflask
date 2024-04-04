from flask import Flask, jsonify
import os
app = Flask(__name__)

@app.route('/')
def index():
    return 'Helloooooooooooo+'


@app.route('/about')
def index():
    return "We accept the fight"

if __name__ =="__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))

