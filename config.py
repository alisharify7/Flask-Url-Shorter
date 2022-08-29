db_name="app.db"
# set on default in flask 
host="https://127.0.0.1:5000/"

class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_name}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
    

class Development(Config):
    DEBUG=True
    FLASK_DEBUG=True


class Production(Config):
    DEBUG=False
    FLASK_DEBUG=False
