from flask import Flask, redirect, render_template, request, url_for, send_from_directory
import pandas as pd

app = Flask(__name__)

todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form['todo']
    todos.append(todo)
    return redirect(url_for('index'))

@app.route('/remove/<int:index>')
def remove(index):
    del todos[index-1 ]
    return redirect(url_for('index'))

@app.route('/download_todos')
def download():
    df = pd.DataFrame({
        'todo_id': list(range(len(todos))),
        'todo': todos
    })