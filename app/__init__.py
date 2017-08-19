# -*- coding: utf-8 -*-
import os

from flask import Flask

from conf.app import APP_CONF


def create_app():
    app = Flask(__name__)

    env = os.environ.get('app_env')
    app.config.from_object(APP_CONF.get(env))
    print app.config

    from .model import db
    return app