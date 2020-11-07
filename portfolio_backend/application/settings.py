from portfolio_backend.application.config import BASE_DIR, ROOT_DIR, SECRETS


class BackendSettings:
    # Header application settings:
    SECRET_KEY = SECRETS["SECRET_KEY"]
    # Header paths:
    ROOT_DIR = ROOT_DIR
    BASE_DIR = BASE_DIR
    # Static and media files:
    DATA_DIR = f"{ROOT_DIR}/data"
    STATIC_DIR = f"{BASE_DIR}/static"
    DATA_URL = "/data/"
    STATIC_URL = "/static/"
    # Database:
    DATABASE_SQLITE_FILE_PATH = f"{ROOT_DIR}/database.db"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE_SQLITE_FILE_PATH}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # Admin:
    FLASK_ADMIN_SWATCH = "flatly"
