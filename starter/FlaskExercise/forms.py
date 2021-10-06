from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from Flask_wtf import SubmitField

class AnimalForm(FlaskForm):
    image_path = FileField('Image', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Save')
