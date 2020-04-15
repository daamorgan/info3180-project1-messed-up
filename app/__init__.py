from flask import Flask
from flask_sqlalchemy import SQLAlchemy

UPLOAD_FOLDER='./app/static/uploads'
app=Flask(__name__)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.config['SECRET_KEY']="Xz9am$hu7gry"
app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_URL='postgresql://ljbxsvxojiuslh:18dc0343fac9a78f606ae0d46485550e3b74e71e6095dfea4e014a041c9086fa@ec2-3-211-48-92.compute-1.amazonaws.com:5432/dd4gj1qiq7naad' #"postgres://project1:password123@localhost/project1" 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

app.config.from_object(__name__)
from app import views, models