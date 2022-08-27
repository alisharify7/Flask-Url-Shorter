class Config:
    DEBUG=True
    FLASK_DEBUG=True
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    SECRET_KEY = "hello world! :) so safe"
