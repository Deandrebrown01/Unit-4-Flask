from flask import Flask, render_template,request,redirect
import pymysql

Goals =['Go to the gym more','Get a new outfit', 'Learn how to make a filipino dish']

app = Flask (__name__)
con = pymysql.Connect(
    database="dbrown_todos",
    user="dbrown",
    password= "228370052",
    host="10.100.33.60",
    cursorclass= pymysql.cursors.DictCursor
)

@app.route('/',methods = ['GET', 'POST'])
def Index():
    if request.method =='POST':
        new_todo = request.form["new_todo"]
        cursor = con.cursor()
        cursor.execute(f"INSERT INTO `todos` (`description`) VALUES ('{new_todo}')")
        cursor.close()
        con.commit()

    cursor = con.cursor()
    cursor.execute("SELECT * FROM `todos` ORDER BY `complete`")

    results = cursor.fetchall()
    cursor.close()

    return render_template("todo.html.jinja", My_Goals = results)

@app.route('/complete_todo/<int:todo_index>',methods = ['POST'])
def complete_todo(todo_index):
    cursor = con.cursor()

    cursor.execute(f"UPDATE `todos` SET `complete` = 1 WHERE `id` = {todo_index}  ")

    cursor.close()
    con.commit()

    return redirect('/')


@app.route('/delete_todo/<int:todo_index>',methods = ['POST'])
def todo_delete(todo_index):


    return redirect('/')
   




