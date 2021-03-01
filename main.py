from flask import Flask

app=Flask(__name__)


@app.route("/")
def home():
    title="home page"
    content="home"
    html_temp=f"""
    <head>
        <title>{title}</title>
    </head>
    <body>
    <h1>{content}</h1>
    <a href='/'>home</a>
    <a href='/product'>product</a>
    <a href='/about'>about</a>   
    <a href='/help'>help</a>
    <a href='/contact'>contact</a>  
    </body>
    </html>
    """
    return html_temp


@app.route("/product")
def product():
    title="product page"
    content="product"
    html_temp=f"""
    <head>
        <title>{title}</title>
    </head>
    <body>
    <h1>{content}</h1>
    <a href='/'>home</a>
    <a href='/product'>product</a>
    <a href='/about'>about</a>   
    <a href='/help'>help</a>
    <a href='/contact'>contact</a>  
    </body>
    </html>
    """
    return html_temp


# @app.route("/help")
# def help():
#     return html_home


# @app.route("/about")
# def about():
#     return html_home


# @app.route("/contact")
# def contact():
#     return html_home


app.run(debug=True)