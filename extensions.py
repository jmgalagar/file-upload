# extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager # NOTE: New import

db = SQLAlchemy()
jwt = JWTManager() # NOTE: New JWT extension initialization