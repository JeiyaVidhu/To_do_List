from flask import Flask, render_template, request, redirect, url_for
from dbfunctions import add_new_task, get_complete_tasks, get_incomplete_tasks, mark_task_as_complete

app = Flask(
    __name__,
    template_folder='CLIENT/TEMPLATES'

)

@app.route("/")
def Create():
    complete = get_complete_tasks()
    incomplete = get_incomplete_tasks()
    return render_template('Create.html', complete=complete, incomplete=incomplete)

@app.route("/add", methods=['POST'])
def add():
    task = request.form['todoitem']
    add_new_task(task)
    return redirect(url_for('Create'))

@app.route("/complete/<task>")
def complete(task):
    mark_task_as_complete(task)
    return redirect(url_for('Create'))


if __name__ == '__main__':
    app.run(debug=True)