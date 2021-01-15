class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://Diet Plan:floyd@localhost:5433/diet plan'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'super-secret-key'
    JWT_ERROR_MESSAGE_KEY = 'message'
