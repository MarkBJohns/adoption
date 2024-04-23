from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    '''Add a pet for adoption'''
    
    name = StringField('Pet Name', validators=[InputRequired()])
    species = SelectField(
        'Species', validators=[InputRequired()],
        choices=[('cat', 'cat'), ('dog', 'dog'), ('porcupine', 'porcupine')])
    photo_url = StringField('Picture', validators=[Optional(), URL(require_tld=True, message='Invalid URL')])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField('Notes', validators=[Optional()])