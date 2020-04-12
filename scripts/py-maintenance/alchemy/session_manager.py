from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
import urllib


#engine = create_engine('postgres://testuser:test1234@127.0.0.1/altium_test')

params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client "
                                 "10.0};SERVER=localhost;DATABASE=altium_db;UID=librarian;PWD=test1234")
engine = create_engine("mssql+pyodbc://librarian:test1234@localhost/altium_db?driver=SQL+Server+Native+Client+11.0")
metadata = MetaData(bind=engine)
