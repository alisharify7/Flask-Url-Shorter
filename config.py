db_name="app.db"
host=f"http://127.0.0.1:5000"

class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_name}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # default secret key From flask own doc
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
    

class Development(Config):
    DEBUG=True
    FLASK_DEBUG=True


class Production(Config):
    DEBUG=False
    FLASK_DEBUG=False
