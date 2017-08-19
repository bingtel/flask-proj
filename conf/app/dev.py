# -*- coding: utf-8 -*

from .common import *

DB_POOL_CONF = dict(
    max_connections=8,
    stale_timeout=300,
    host="localhost",
    port=3306,
    user="root",
    passwd="password"
)