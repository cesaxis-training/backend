from flask import Flask
from src.routes.db_access import db_test_blueprint


def create_app():
    app = Flask(__name__)

    # Register the db_test blueprint from db_access.py
    app.register_blueprint(db_test_blueprint)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)


def runme():
    return 1
