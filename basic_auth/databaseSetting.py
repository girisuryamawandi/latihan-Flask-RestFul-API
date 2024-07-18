from config import *
class Config:
    uri_database = f'mysql+pymysql://{user}:{password}@{database_ip}/{database_name}'
    print(uri_database)
    SQLALCHEMY_DATABASE_URI =  uri_database
    SQLALCHEMY_TRACK_MODIFICATIONS = False