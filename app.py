from flask import Flask, render_template, request
import db_interaction

app = Flask(__name__)
app.secret_key = "MUVETSOssIHYJGeeNM3"

@app.route('/')
def home():
    tasks = db_interaction.get_sorted_tasks_list()
    return render_template("home.html", tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    todo = str(request.form["todo"])
    try:
        urgent_return = request.form["urgent"]
        if urgent_return == 'on':
            urgent = 1
        else:
            urgent = 0
    except:
        urgent = 0

    if todo:
        result = db_interaction.db_insert_task(todo, urgent)
        if (result>0):
            tasks = db_interaction.get_sorted_tasks_list()
            return render_template("home.html", tasks=tasks)

@app.route('/delete')
def delete(task):
    db_interaction.db_remove_task(task)
    tasks = db_interaction.get_sorted_tasks_list()
    return render_template("home.html", tasks=tasks)

if __name__ == '__main__':
    db_interaction.initiate_db()
    app.run(debug=True)

