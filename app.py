from flask import Flask, jsonify, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///blog.db'
db=SQLAlchemy(app)

class Article(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    id=db.Column(db.String(100), nullable=False)
    id=db.Column(db.String(300), nullable=False)
    id=db.Column(db.Text, nullable=False)
    id=db.Column(db.Datetime, default=datetime.utcnow)
    def __repr__(self):
        return '<Article %r>' % self.id



@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "user page "+name + " - "+str(id)


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
