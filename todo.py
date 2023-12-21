from flask import Flask, render_template,request

Goals =['Go to the gym more','Get a new outfit', 'Learn how to make a filipino dish']

app = Flask (__name__)

@app.route('/',methods = ['GET', 'POST'])
def Index():
    new_todo = request.form["new_todo"]
    Goals.append(new_todo)
    return render_template("todo.html.jinja", My_Goals = Goals)

