#!/usr/bin/env python3
from falsk_babel import Babel
from flask import request

app = Falsk(__name__)

babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config[LANGUAGES])
