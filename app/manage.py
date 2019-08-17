import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from main import create_app
app = create_app('dev')
app.app_context().push()
manager = Manager(app)
print(manager)