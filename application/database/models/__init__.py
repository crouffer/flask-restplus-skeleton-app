from ..flask_db import get_db

db = get_db()


class ExampleDatabaseModel(db.Model):
    """
    An Example Database Model
    """
    __tablename__ = "example_database_model"
    id = db.Column(db.Integer, primary_key=True)
    date_added = db.Column(db.DateTime, default=db.func.now(), nullable=True)
    string_column = db.Column(db.String, nullable=False)
