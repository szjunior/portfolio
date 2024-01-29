from flask import Flask, render_template, abort

app = Flask(__name__)

projects = [
    {
        "name":"Documentation Python / Flask / Jinja",
        "thumb": "img/habit-tracking.png",
        "hero": "img/habit-tracking.png",
        "categories": ["writing"],
        "slug": "api-docs",
    },
    {   
        "name":"Habit Tracking App with Python and MongoDB",
        "thumb": "img/personal-finance.png",
        "hero": "img/personal-finance.png",
        "categories": ["python", "web"],
        "slug": "habit-tracking",
    },
    {   
        "name":"Personal Finance Tracking App with Python / React",
        "thumb": "img/rest-api-docs.png",
        "hero": "img/rest-api-docs.png",
        "categories": ["react", "Java"],
        "slug": "personal-finance",
    },
]

slug_to_project = {project["slug"]: project for project in projects}

@app.route('/')
def home():
    return render_template('home.html', projects=projects)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    try:
        return render_template(
        f"project_{slug}.html", 
        project=slug_to_project[slug]
    )
    except page_not_found:
        abort(404)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
