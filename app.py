#!/usr/bin/env python
'''
app.py

Gliders Homepage
'''

from flask import Flask, url_for
from flask_environments import Environments
import os

app = Flask('gliders')

from gliders.reverse_proxy import ReverseProxied
app.wsgi_app = ReverseProxied(app.wsgi_app)


# Configuration
env = Environments(app, default_env='DEVELOPMENT')
env.from_yaml('config.yml')
if os.path.exists('config.local.yml'):
    env.from_yaml('config.local.yml')

if app.config['LOGGING'] == True:
    import logging
    logger = logging.getLogger('oceansmap.app')
    logger.setLevel(logging.DEBUG)

    log_directory = app.config['LOG_FILE_PATH']
    log_filename = os.path.join(log_directory,app.config['LOG_FILE'])
    if not os.path.exists(os.path.dirname(log_filename)):
        os.makedirs(os.path.dirname(log_filename))
    file_handler = logging.FileHandler(log_filename, mode='a+')

    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(process)d - %(name)s - %(module)s:%(lineno)d - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)
    #app.logger.addHandler(stream_handler)
    app.logger.setLevel(logging.DEBUG)
    app.logger.info('Application Process Started')

from gliders import gliders
app.register_blueprint(gliders, url_prefix='')

@app.context_processor
def url_process():
    def url_root():
        return url_for('.show_index')
    return {'url_root': url_root}


if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])

