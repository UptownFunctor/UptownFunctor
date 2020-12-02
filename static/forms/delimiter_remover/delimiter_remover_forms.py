from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired

class TextAreaForm(FlaskForm):

    inputTextArea = TextAreaField('Input Text Here', validators=[DataRequired()])
    outputTextArea = TextAreaField('Delimited Text')
    delimiterInput = StringField('Delimiter to Remove', validators=[DataRequired()])
    submit = SubmitField('Remove Delimiter')