from flask_wtf import Form
from wtforms import StringField


class DecodeURL(Form):
    url = StringField(
        'Enter URL'
    )
