import json
import os
from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import InputRequired
from wtforms.validators import ValidationError

class DeleteForm(Form):
    name = TextField('', [InputRequired()])

    def validate_name(form, field):
        if form.name.data != "":
            raise ValidationError('This username does not exist.')

class DeleteJsonParser():
    def __init__(self):
        self.file = os.path.join('user/users.json')
    def write(self, data):
        with open(self.file, 'w') as f:
            f.write(json.dumps(data, indent=2))
    def read(self):
        if not os.path.exists(self.file):
            return {}
        with open(self.file) as f:
            data = json.loads(f.read())
        return data
    def delete_user(self, name):
        users = self.read()
        if not users.pop(name):
            return False
        self.write(users)
        return True