class Config:
    DEBUG=True
    FLASK_DEBUG=True
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    secret_key = b'_5#y2L"F4Q8z\n\xec]/'


class Development(Config):
    SECRET_KEY = "hello world! :) so safe"
