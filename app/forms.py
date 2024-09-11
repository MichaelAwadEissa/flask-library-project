from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    cover_photo = FileField('Cover Photo', validators=[DataRequired()])
    pages = IntegerField('Number of Pages', validators=[DataRequired(), NumberRange(min=1)])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')
