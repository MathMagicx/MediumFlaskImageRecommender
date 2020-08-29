import os

class developmentConfig:
    SECRET_KEY = '[\xaa$I"*\xdd$85]D\x12\x02\x8d\x97\xf0\x1fU\xb7\x8c\rA\xe8'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///gallery.db'
class productionConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')