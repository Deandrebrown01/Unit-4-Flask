from flask import Flask, render_template,request,redirect
import pymysql

Goals =['Go to the gym more','Get a new outfit', 'Learn how to make a filipino dish']

app = Flask (__name__)

@app.route('/',methods = ['GET', 'POST'])
def Index():
    if request.method =='POST':
        new_todo = request.form["new_todo"]
        Goals.append(new_todo)
        con = pymysql.Connect(
            database= Goals,
            user="dbrown",
            password= "228370052",
            host="10.100.33.60",
            cursorclass= pymysql.cursors.DictCursor

        )
        cursor = con.cursor()

        cursor.execute("SELECT ``, FROM ``")

        results = cursor.fetchall()



        
        
    
    return render_template("todo.html.jinja", My_Goals = Goals)



@app.route('/delete_todo/<int:todo_index>',methods = ['POST'])
def todo_delete(todo_index):
    del Goals[todo_index]


    return redirect('/')
   




