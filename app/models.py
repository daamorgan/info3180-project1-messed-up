from . import db

class Profile(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    firstname=db.Column(db.String(80), nullable=False)
    lastname=db.Column(db.String(80), nullable=False)
    gender=db.Column(db.String(80), nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    location=db.Column(db.String(245), nullable=False)
    biography=db.Column(db.Text(), nullable=False)
    date=db.Column(db.String(80), nullable=False)
    filename=db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, firstname, lastname, gender, email, location, biography, date, filename):
        self.firstname=firstname
        self.lastname=lastname
        self.gender=gender
        self.email=email
        self.location=location
        self.biography=biography
        self.date=date
        self.filename=filename

    def __repr__(self):
        return '<Profile %r>' % self.firstname #IS THIS CORRECT