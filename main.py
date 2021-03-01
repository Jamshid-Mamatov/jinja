from flask import Flask

app=Flask(__name__)

html_home="<h1>HTML HOME</h1>"

@app.route("/")
def home():
    link="""
    <a href='/product'>product</a>
    <a href='/about'>about</a>
    <a href='/help'>help</a>
    <a href='/contact'>contact</a>
    """

    return link

@app.route("/product")
def product():
    return "salom"

@app.route("/help")
def help():
    return html_home

@app.route("/about")
def about():
    return html_home

@app.route("/contact")
def contact():
    return html_home
app.run(debug=True)