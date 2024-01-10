# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Use SQLite for simplicity
db = SQLAlchemy(app)

from app import routes  # Import routes at the end to avoid circular import
