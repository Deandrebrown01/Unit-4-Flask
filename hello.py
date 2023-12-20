from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template("home.html.jinja")

@app.route('/ping')
def Ping():
    return "<h1> Pong <h1>"
@app.route('/hello/<name>')
def hello(name):
    return(f"hello {name}")







