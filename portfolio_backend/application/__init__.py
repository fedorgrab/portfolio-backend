# fmt: off
import os
import sys

from flask import Flask
from flask_admin import Admin
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from portfolio_backend.application.settings import BackendSettings

sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), "../", "../")))

backend_application = Flask(
    import_name=__name__,
    template_folder=f"{BackendSettings.BASE_DIR}/templates/"
)

backend_application.config.from_object(BackendSettings)
CORS(backend_application)

db = SQLAlchemy(backend_application)
migrate = Migrate(backend_application, db)
ma = Marshmallow(backend_application)
admin = Admin(backend_application, name="portfolio", template_mode="bootstrap3")

from portfolio_backend import admin  # noqa
from portfolio_backend import models  # noqa
from portfolio_backend import routes  # noqa
from portfolio_backend import schemas  # noqa
# fmt: on
