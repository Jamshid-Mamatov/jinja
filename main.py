from flask import Flask
from jinja2 import Template
app=Flask(__name__)

html_temp=Template("""
    <head>
        <title>{{title}}</title>
    </head>
    <body>
    <h1>{{content}}</h1>
    <a href='/'>home</a>
    <a href='/product'>product</a>
    <a href='/about'>about</a>   
    <a href='/help'>help</a>
    <a href='/contact'>contact</a>  
    </body>
    </html>
    """)

@app.route("/")
def home():
    title="home page"
    content="home"
    
    return html_temp.render(title=title,content=content)


@app.route("/product")
def product():
    title="product page"
    content="product"
    
    return html_temp.render(title=title,content=content)


@app.route("/help")
def help():
    title="help page"
    content="help"
    return html_temp.render(title=title,content=content)


@app.route("/about")
def about():
    title="about page"
    content="about"
    return html_temp.render(title=title,content=content)


@app.route("/contact")
def contact():
    title="content page"
    content="content"
    return html_temp.render(title=title,content=content)


app.run(debug=True)