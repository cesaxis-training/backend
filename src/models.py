from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Quotes(db.Model):
    __tablename__ = "quotes"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    author = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Quote {self.id}: {self.text} - {self.author}>"
