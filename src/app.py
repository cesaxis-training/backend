from flask import Flask
from routes.db_access import db_test_blueprint  # Import the db_test blueprint from db_access.py in the routes folder
import os
from models import models

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.environ.get('MYSQL_USER')}:{os.environ.get('MYSQL_PASSWORD')}@{os.environ.get('MYSQL_HOST')}/{os.environ.get('MYSQL_DATABASE')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Register the db_test blueprint from db_access.py
    app.register_blueprint(db_test_blueprint)
    models.db.init_app(app)
    return app


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        models.db.create_all()
    app.run(debug=True)


def runme():
    return 1
