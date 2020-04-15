from .forms import ProfileForm
from datetime import date
from app import db,app
from app.models import Profile
from werkzeug.utils import secure_filename
from flask import render_template, request, redirect, url_for, flash
import os


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form=ProfileForm() 
    if request.method=='POST':
        if form.validate_on_submit():
            date_joined=date.today().strftime("%B %d, %Y")##NB SIR MADE A SEPARATE FUNCTION FOR DATE IN LAB2
            photo=form.photo.data
            filename = secure_filename(photo.filename)
            biography=request.form['biography']
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            newprofile=Profile(request.form['firstname'],request.form['lastname'],request.form['gender'],request.form['email'],request.form['location'], biography.strip() ,date_joined,filename)
            db.session.add(newprofile)
            db.session.commit()##Need to add it to database
            flash("The profile was successfully created.", 'success')
            return redirect('/profiles')
        else:
            flash ("Incorrect data has been entered.Please try again.", 'danger')
    return render_template("form.html", form=form)

@app.route('/profiles')
def profiles():
    profileList = db.session.query(Profile).all()

    return render_template("profile_list.html", profileList=profileList)

@app.route('/profiles/<userid>')
def userpage(userid):
    profile= Profile.query.get(userid)
    return render_template('view_profile.html', profile=profile)


@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")