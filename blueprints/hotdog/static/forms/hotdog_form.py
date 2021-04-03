from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField

print('in form')

class FileUploadForm(FlaskForm):
    file_wtf = FileField('File', validators=[FileRequired()])
    submit_wtf = SubmitField('Submit')