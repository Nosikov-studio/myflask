from flask import Flask, jsonify, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///blog.db'


app.config['SQLALCHEMY_BINDS']={'second_db': 'sqlite:///second_db.db'}
#db2=SQLAlchemy(app)
#db2.init_app(app)
db=SQLAlchemy(app)
class Article(db.Model):
    
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100), nullable=False)
    intro=db.Column(db.String(300), nullable=False)
    text=db.Column(db.Text, nullable=False)
    #date=db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id

class User2(db.Model):
    __bind_key__ = 'second_db'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/posts')
def posts():
    articles=Article.query.first()
    articles=Article.query.all()
    return render_template("posts.html", articles=articles)


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "user page "+name + " - "+str(id)

@app.route('/create', methods=['POST','GET'])
def create():
    if request.method=="POST":
        title=request.form['title']
        intro=request.form['intro']
        text=request.form['text']

        article=Article(title=title, intro=intro, text=text)
        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/posts')
        except:
            return "Errrrrrrrrr!!!"
    else: 
        return render_template("create.html")








if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
