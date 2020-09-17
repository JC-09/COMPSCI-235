# people_web_app

from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from people_web_app.people_blueprint import people
        app.register_blueprint(people.people_blueprint)
