from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample initial todo list
todos = ['Learn Python', 'Build a todo app', 'Deploy the app']

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    todo = request.form['todo']
    todos.append(todo)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_todo(index):
    del todos[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
