"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')
    rows = request.args.get('rows')

    first, last, github = hackbright.get_student_by_github(github)

    projects = hackbright.get_grades_by_github(github)

    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github,
                            projects=projects)
    
    return html


@app.route("/student-search")
def get_student_form():
    """show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/add_student", methods=['POST'])
def student_add():
    """add student"""

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')

    hackbright.make_new_student(first_name, last_name, github)

    html = render_template("succesful_add.html", 
                                first_name=first_name,
                                last_name=last_name,
                                github=github)

    return html

@app.route("/project")
def show_projects():
    """show all project and information"""

    title = request.args.get('project_title')

    hackbright.get_project_by_title(title)

    html = render_template("project_info.html",
                                title=title,
                                description=description,
                                max_grade=max_grade)

    return html

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
