from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, HiddenField
from wtforms.validators import InputRequired, Optional, NumberRange, URL


class AddPetForm(FlaskForm):

    name = StringField("Name",
                       validators=[InputRequired()])
    species = SelectField("Species",
                       choices=[('Cat', 'Cat'),  ('Dog', 'Dog'),  ('Porcupine', 'Porcupine')])
    photo_url = StringField("Photo",
                       validators=[Optional(), URL(require_tld=True, message="Must be valid URL")])
    age = IntegerField("Age",
                       validators=[Optional(), NumberRange(min=0, max=30, message="Age must be between 0 and 30")])
    notes = StringField("Notes",
                       validators=[Optional()])


class EditPetForm(FlaskForm):

    photo_url = StringField("Photo",
                       validators=[Optional(), URL(require_tld=True, message="Must be valid URL")])
    notes = StringField("Notes",
                       validators=[Optional()])
    available = BooleanField("Available",
                        validators=[Optional()])
