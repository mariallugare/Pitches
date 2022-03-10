from flask_wtf import FlaskForm
from wtforms import SelectField,TextAreaField,SubmitField

class PitchForm(FlaskForm):
  category = SelectField('Category', choices=[('-----','-----'),('friendship ','friendship'), ('Inspirational','Inspirational'), ('discussion', 'discussion')])
  content = TextAreaField('Pitch Content')
  submit = SubmitField('Submit')

class CommentForm(FlaskForm):
  comment = TextAreaField('')
  submit = SubmitField('Submit')