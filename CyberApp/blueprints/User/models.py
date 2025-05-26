from app import db


class User(db.Model):
    __tablename__ = 'Users'
    uid = db.Column(db.Integer, primary_key=True, nullable=False)
    Name = db.Column(db.Text, nullable=False)
    Password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Welcome {self.Name}, You logged In!!"
