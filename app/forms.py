from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileRequired, FileAllowed

class ProfileForm(FlaskForm):
    firstname=StringField('First Name', validators=[DataRequired()])
    lastname=StringField('Last Name', validators=[DataRequired()])
    gender=SelectField('Gender', choices=[('','Select Gender'),('Female','female'), ('Male', 'male')], validators=[DataRequired()])##Is the validator needed.
    email=StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder":" e.g. jdoe@example.com"})
    location=StringField('Location', validators=[DataRequired()], render_kw={"placeholder":' e.g. Kingston, Jamaica'})
    biography=TextAreaField('Biography', validators=[DataRequired()])
    photo=FileField(' Profile Picture', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])