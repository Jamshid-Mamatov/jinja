from flask import Flask,render_template
from jinja2 import Template
import json
app=Flask(__name__)


country_data=json.loads(open("country.json").read())


@app.route("/home")
@app.route("/")
def home():
    title="home page"
    content="home"
    
    img_url=country_data[:5]
    
    
    return render_template("home.html",title=title,content=content,img_url=img_url)


@app.route("/product")
def product():
    title="product page"
    content="product"
    
    return render_template("home.html",title=title,content=content)


@app.route("/help")
def help():
    title="help page"
    content="help"
    return render_template("home.html",title=title,content=content)


@app.route("/about")
def about():
    title="about page"
    content="about"
    return render_template("home.html",title=title,content=content)


@app.route("/contact")
def contact():
    title="content page"
    content="content"
    return render_template("home.html",title=title,content=content)


app.run(debug=True)