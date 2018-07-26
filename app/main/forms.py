from flask import request
from flask_wtf import FlaskForm
from flask_babel import _, lazy_gettext as _l
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Length
from app.models import User


class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_l('About me'), validators=[Length(min=0, max=140)])
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *arg, **kwargs):
        super(EditProfileForm, self).__init__(*arg, **kwargs)
        self.original_username = original_username

    def validiate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidiationError(_('Please use different username.'))

class PostForm(FlaskForm):
    post = TextAreaField(_l('Say Something'), validators=[ DataRequired(), Length(min=1, max=140) ])
    submit = SubmitField(_l('submit'))