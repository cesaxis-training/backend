import logging
import sys  # Import sys to access stdout
from flask import Flask
from routes import quote_bp
from flask_cors import CORS
import models
from config import Config  # Import the Config class

logger = logging.getLogger(__name__)
# Configure logging to stdout
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG if Config.FLASK_ENV == 'development' else logging.INFO)  # Set logging level based on environment
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.setLevel(logging.INFO)
logger.addHandler(handler)

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://"
        f"{Config.MYSQL_USER}:{Config.MYSQL_PASSWORD}"
        f"@{Config.MYSQL_HOST}/{Config.MYSQL_DATABASE}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    CORS(app)
    # Register the db_test blueprint from db_access.py
    app.register_blueprint(quote_bp)
    models.db.init_app(app)

    logger.info("App created and configured successfully.")

    return app


if __name__ == "__main__":
    logger.info("Starting application...")
    app = create_app()
    logger.info("Application instance created")

    with app.app_context():
        logger.info("Creating database tables...")
        try:
            models.db.create_all()
            logger.info("Database tables created successfully")
        except Exception as e:
            logger.error(f"Failed to create database tables: {str(e)}")
            raise

    logger.info(f"Starting Flask server in {Config.FLASK_ENV} mode...")
    app.run(debug=Config.FLASK_ENV == 'development')
    logger.info("Flask server stopped")


def runme():
    return 1
