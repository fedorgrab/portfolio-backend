# fmt: off
import sys
import os

sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), "../", "../")))
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from portfolio_backend.application.settings import BackendSettings

backend_application = Flask(
    import_name=__name__,
    # static_url_path="/static/",
    # static_folder=f"{BackendSettings.BASE_DIR}/static",
    # template_folder=f"{BackendSettings.BASE_DIR}/frontend"
)
backend_application.config.from_object(BackendSettings)

db = SQLAlchemy(backend_application)
migrate = Migrate(backend_application, db)
admin = Admin(backend_application, name="portfolio", template_mode="bootstrap3")

from portfolio_backend import models  # noqa
from portfolio_backend import routes  # noqa
from portfolio_backend import admin  # noqa
# fmt: on
