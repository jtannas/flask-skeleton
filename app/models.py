"""SQLAlchemy Table Definitions"""
### IMPORT & INIT #####################################################
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()
db_now = db.func.current_timestamp


### TEMPLATE ##########################################################
class ModelTable(db.Model):
    """Base model tabledef to inherit"""
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db_now())
    modified_at = db.Column(db.DateTime, default=db_now(), onupdate=db_now())


### TABLEDEFS #########################################################
class User(ModelTable, UserMixin):
    """Database User Table Model"""
    __tablename__ = "users"

    email = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(128), nullable=True)
    active = db.Column(db.Boolean(), default=False)
    tokens = db.Column(db.Text)