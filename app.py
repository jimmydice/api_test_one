"""Main module for initializing the Flask application"""
import os
from flask import Flask
from flask_cors import CORS
from api.models import db
from api.routes import api_bp

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Ensure the 'instance' directory exists
instance_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance')
if not os.path.exists(instance_path):
    os.makedirs(instance_path)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(instance_path, 'videogames.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
