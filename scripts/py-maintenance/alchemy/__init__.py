from .encoders import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
from configuration.config_manager import app_config


__connection_string = 'mssql+pyodbc://' + app_config['databases']['mssql']['username'].get() + \
                      ':' + app_config['databases']['mssql']['password'].get() + \
                      '@' + app_config['databases']['mssql']['host'].get() + \
                      '/' + app_config['databases']['mssql']['database'].get() + \
                      '?driver=' + app_config['databases']['mssql']['driver'].get()

__engine = create_engine(__connection_string)
metadata = MetaData(bind=__engine)
sessionmaker = sessionmaker(__engine)
