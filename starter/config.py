import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'eng1.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'Dingabo'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'ai5580'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Elahikhair_786'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'engstorage2'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'lPLIM2IeodJVREwvqefKbY0IFAGhGtu8nfgmVA9rCMQaS1WVQjHHF0NJjbdk3sg3m6Ilc8P+78WvTpl0/0Bfiw=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'img'

