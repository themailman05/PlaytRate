from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired

class SearchForm(Form):
    searchquery = StringField('searchquery', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
