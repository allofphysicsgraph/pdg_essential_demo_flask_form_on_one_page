#!/usr/bin/env python3
# Ben Payne
# Physics Derivation Graph
# https://allofphysics.com
# Creative Commons Attribution 4.0 International License
# https://creativecommons.org/licenses/by/4.0/

import random

from flask import Flask, render_template, request

# https://github.com/hplgit/web4sciapps/blob/master/doc/src/web4sa/src-web4sa/apps/flask_apps/vib1/model.py
from wtforms import Form, TextField, SelectField, validators

class InputForm(Form): # http://wtforms.simplecodes.com/docs/0.6.1/fields.html
    input_expression  = TextField(u'Input Expression', [validators.required()])
    inference_rule    = SelectField(u'inference rule', choices=[('multbothsidesby', 'multiply both sides by'), 
                                                                ('simplify', 'simplify'), 
                                                                ('dividebothsidesby', 'divide both sides by')])
    feed              = TextField(u'Feed', [validators.required()])
    output_expression = TextField(u'Output Expression', [validators.required()])



def compute(input_expression,inference_rule,feed,output_expression):
    return random.randint(100,999),random.randint(100,999)

web_app = Flask(__name__)

@web_app.route('/', methods=['GET', 'POST'])
def index():
    # https://flask.palletsprojects.com/en/stable/quickstart/#rendering-templates
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = compute(form.input_expression.data, 
                         form.inference_rule.data,
                         form.feed.data,
                         form.output_expression.data)
    else:
        result = None

    return render_template('view.html', form=form, result=result)


if __name__ == '__main__':
    web_app.run(debug=True, host="0.0.0.0")

