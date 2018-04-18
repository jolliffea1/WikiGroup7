import json
import os
from flask_wtf import Form
from wtforms import BooleanField
from wtforms import TextField
from wtforms import TextAreaField
from wtforms import PasswordField
from wtforms.validators import InputRequired
from wtforms.validators import ValidationError

class MyJsonParser():

    def __init__(self):
        self.file = os.path.join('user/users.json')

    def read(self):
        if not os.path.exists(self.file):
            return {}
        with open(self.file) as f:
            data = json.loads(f.read())
        return data

    def write(self, data):
        with open(self.file, 'w') as f:
            f.write(json.dumps(data, indent=2))

    def add_user(self, name, password, roles=[]):
        users = self.read()
        if users.get(name):
            return False
        new_user = {
            'active': True,
            'roles': roles,
            'authentication_method': 'cleartext',
            'authenticated': True
        }
        users[name] = new_user
        self.write(users)

class UserForm(Form):
    username = TextField('', [InputRequired()])
    password = TextField('', [InputRequired()])
    roles = TextField('',[InputRequired()])

    def validate_name(form, field):
        if field.data == '':
            raise ValidationError('This username does not exist.')

    def validate_password(form, field):

        if form.username.data == '':
            raise ValidationError('Username and password do not match.')
