# Altium DBlib API
This repository contains a Python Restful API that manages a MSSQL database to be used as an Altium's DBLib.
The project is based on:
- SQL Server
- Flask and Flask extensions like Flask-Restful, Flask-SQLAlchemy, Flask-Migrations, etc.
- SQLAlchemy

##Organization
- *SQL* directory: Contains the all the views that formats database data into something that Altium can understand. The 
data in the DB is structured in a multiple table manner but Altium queries a single table for component, symbols and 
footprints data. This views format that multi-table information into a single table.
- *sources* directory: The Python API

##Enviroment
The application is meant to be runned as a Docker container. In order to configure the container the following environment variables
cab be used:
- SECRET_KEY: Flask secret used for cookies signing among others
- FLASK_ENV: The environment where the app is deployed. Typical values are: DEV, STAG, PROD, etc...
- FLASK_APP: This value is harcoded inside the Docker image to be *app/wsgi.py*
- FLASK_DEBUG
- SQLALCHEMY_DATABASE_URI: Database URI. This application is meant to be used with a MSSQL database, so this URI would be likely similar to this one:  
```mssql+pyodbc://<USER>:<PASSWORD>@<DB_HOST>/<DB>?driver=ODBC+Driver+17+for+SQL+Server```  
Keep in mind that the above example works only for SQL authentication. ODBC driver MUST be in place before running the application.  
For more information about the ODBC driver check out this [link](https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15)
- SQLALCHEMY_ECHO: Turns on/off the SQL output
- APP_LOG_LEVEL: Application-wise log level