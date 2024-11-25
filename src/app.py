from flask import Flask
from routes.hello_world  import example_blueprint

def create_app():
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(example_blueprint)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
