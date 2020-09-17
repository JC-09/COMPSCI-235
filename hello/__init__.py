#__init__.py
from flask import Flask, render_template


# wsgi.py will execute the following functions

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return 'Homepage'

    @app.route('/greet/<name>')
    def say_hello(name: str): # The value of name is provided in the url, e.g. http://localhost:5000/greet/Jonathan will produce "Hello, Jonathan"
        return render_template('hello.html', name=name)

    @app.route('/people')
    def list_people():
        list_of_people = ['Mohandas Gandhi', 'Nelson Mandela', 'Martin Luther King', 'Abraham Lincoln',
                          'George Washington', 'Napolean Bonaparte', 'Franklin Roosevelt', 'Winston Churchill']
        return render_template('people.html', people=list_of_people)

    @app.route('/<name>')
    def make_html_page(name: str):  # This method renders any extra html pages that were not yet rendered above.
        return render_template(name + '.html', message='Hello!')

    return app
