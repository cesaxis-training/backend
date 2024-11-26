from flask import Blueprint
import mysql.connector
import os

# Create the Blueprint object
db_test_blueprint = Blueprint('db_test', __name__)


# Define the routes inside the blueprint
@db_test_blueprint.route('/hello-world', methods=['GET'])
def hello_world():
    return "Hello, World!", 200


@db_test_blueprint.route('/db-test', methods=['GET'])
def db_test():
    try:
        conn = mysql.connector.connect(
            host=os.environ.get('MYSQL_HOST'),
            user=os.environ.get('MYSQL_USER'),
            password=os.environ.get('MYSQL_PASSWORD'),
            database=os.environ.get('MYSQL_DATABASE')
        )
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE()")
        result = cursor.fetchone()
        conn.close()
        return f"Connected to database: {result[0]}", 200
    except mysql.connector.Error as err:
        return f"Error: {err}", 500
