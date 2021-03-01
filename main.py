from flask import Flask

app=Flask(__name__)

html_home="<h1>HTML HOME</h1>"

@app.route("/")
def home():

    return html_home

app.run(debug=True)