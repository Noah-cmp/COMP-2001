from config import db, ma

class Profile(db.Model):
    __tablename__ = "Profile"
    __table_args__ = {"schema": "CW2"}

    email = db.Column(db.String(30), primary_key=True)
    username = db.Column(db.String(30), nullable=False)

    aboutme = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(50), nullable=True)
    dob = db.Column(db.Date, nullable=True)
    language = db.Column(db.String(30), nullable=True)

    password = db.Column(db.String(30), nullable=False)

    role = db.Column(db.String(5), nullable=False, default="User")  


