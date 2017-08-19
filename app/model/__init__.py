# -*- coding: utf-8 -*-

import os

from peewee import Model
from playhouse.pool import PooledMySQLDatabase

from conf.app import APP_CONF

conf = APP_CONF.get(os.environ.get('app_env'))


db = PooledMySQLDatabase(conf.DB_NAME, **conf.DB_POOL_CONF)


class BaseModel(Model):
    class Meta:
        database = db