from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length 

class EntropyToWordsAndKeys(FlaskForm):
    entropy = StringField('Entropy', validators=[DataRequired(), Length(min=2, max=128)])
    language = RadioField('Language', choices=['Hindi','Tamil','English'] ,validators=[DataRequired(), Length(min=5, max=7)])
    submit = SubmitField('Generate')


### use radio buttons for language
### add option for number of words
### show words in the same line and not as an ordered list
