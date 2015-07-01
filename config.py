# ------------------------------------------------------------------------------
# Config
# ------------------------------------------------------------------------------

import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Should the application be in debug mode?
DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

# Beacons
BEACON_URI = os.getenv('BEACON_URI', "localhost:8080")