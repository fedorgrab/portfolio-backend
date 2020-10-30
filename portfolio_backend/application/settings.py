from portfolio_backend.application.config import BACKEND_CONFIGS as B_CONF
from portfolio_backend.application.config import BASE_DIR, ROOT_DIR


class BackendSettings:
    # Main application settings:
    SECRET_KEY = B_CONF["SECRET_KEY"]
    # Main paths:
    BASE_DIR = BASE_DIR
    DATA_DIR = f"{ROOT_DIR}/data"
    STATIC_DIR = f"{BASE_DIR}/static"
    # Database:
    DATABASE_SQLITE_FILE_PATH = f"{ROOT_DIR}/database.db"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE_SQLITE_FILE_PATH}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # Admin:
    FLASK_ADMIN_SWATCH = "cerulean"
