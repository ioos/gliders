#!/usr/bin/env python
'''
gliders
'''

from flask import Blueprint

gliders = Blueprint('gliders', __name__, static_url_path='', static_folder='static', template_folder='templates')

from gliders.controller import show_root
