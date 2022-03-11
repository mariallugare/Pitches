import os

class Config:

    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://marial:Doralove91!@localhost/pitch_hub2'
    SECRET_KEY = 'marial'
    # SQLALCHEMY_DATABASE_URI ='sqlite:////tmp/test.db'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL','')
    if SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace('postgres://', "postgresql://", 1)
    


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://marial:Doralove91!@localhost/pitch_hub2'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}