from flask import g
from flask_babel import get_locale
# ...
@app.before_request
def before_request():
    # ...
    g.locale = str(get_locale())
