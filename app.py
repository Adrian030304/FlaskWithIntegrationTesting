from flask import Flask, redirect, render_template, request, url_for, send_from_directory

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