import os

class Config:

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://marial:Doralove91!@localhost/pitch_hub'
    SECRET_KEY = 'marial'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL','')
    if SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace('postgres://', "postgresql://", 1)
    


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}