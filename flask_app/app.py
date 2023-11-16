''' Flask app that takes in a artist and song and returns the top 10 similar songs. '''

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from utils.utils import recommend_content
import os

csrf = CSRFProtect()
app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

csrf.init_app(app)
Bootstrap5(app)


class NameForm(FlaskForm):
    artist = StringField('Enter artist name: ', validators=[DataRequired()])
    name = StringField('Enter song name: ', validators=[DataRequired()])
    submit = SubmitField('Submit')

# route for home page
@app.route('/', methods=['GET', 'POST'])
def index():
    ''' 
    Displays a form to enter a song.
    Displays results if form is submitted.
    '''
    form = NameForm()
    if form.validate_on_submit():
        artist = form.artist.data
        name = form.name.data
        similar_songs = recommend_content(artist, name)
        if similar_songs:
            return render_template('index.html', form=form, artist=artist, name=name, similar_songs=similar_songs)
        else:
            message = "That song is not in our database."
            return render_template('index.html', form=form, message=message)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

