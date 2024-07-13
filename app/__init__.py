from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configure your application
    app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with your secret key
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///application.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db)
    CORS(app, supports_credentials=True)

    with app.app_context():
        from . import routes
        routes.init_routes(app)
        db.create_all()
        print("Server Created")

    return app
