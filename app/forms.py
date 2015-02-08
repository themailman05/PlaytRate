from flask.ext.wtf import Form
from wtforms import StringField
from wtforms import BooleanField
from wtforms.validators import DataRequired

class SearchAreaForLocations(Form):
    searchquery = StringField('searchquery', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    yp = BooleanField('yp')

