from flask import Flask, flash, session, request, redirect, render_template, url_for

from db.data_layer import create_project, get_all_projects, get_project, update_project, delete_project
from db.data_layer import create_task, get_all_tasks, get_task, update_task, delete_task

app = Flask(__name__)


@app.route('/')
def index():
    db_projects = get_all_projects()
    return render_template('index.html', projects = db_projects)

@app.route('/add_project', methods=['POST'])
def add_project():
    title = request.form['html_title']
    create_project(title)
    return redirect(url_for('index'))

@app.route('/edit_project/<project_id>')
def edit_project(project_id):
    db_project = get_project(project_id)
    return render_template('edit_proj.html', project = db_project)

@app.route('/update_project', methods=['POST'])
def update_project_request():
    project_id = request.form['html_id']
    title = request.form['html_title']
    update_project(project_id, title)
    return redirect(url_for('index'))

@app.route('/delete_project/<project_id>')
def delete_project_request(project_id):
    delete_project(project_id)
    return redirect(url_for('index'))

@app.route('/list_tasks/<project_id>')
def list_tasks(project_id):
    db_tasklist = get_all_tasks(project_id)
    db_project = get_project(project_id)
    return render_template('list_tasks.html', tasklist = db_tasklist, project = db_project)


@app.route('/add_task', methods=['POST'])
def add_task():
    description = request.form['html_description']
    create_task(project_id, description)
    return render_template('list_tasks.html')

app.run(debug=True)