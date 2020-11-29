# Altium DBlib API

This repo contains an API that manages Altium DBLib databases. Now with component inventory too!  
The API has been build using python 3.8 and all the Flask-Restful ecosystem, that means sqlalchemy and migrations are 
used behind the scenes.

## Organization
- *SQL* directory: Contains the all the views that formats database data into something that Altium can understand. The 
data in the DB is structured in a multiple table manner but Altium queries a single table for component, symbols and 
footprints data. This views format that multi-table information into a single table.
- *sources* directory: The Python API
- *tests* directory: Pytest test of the service layer.
- Altium_DB_Lib_vX.Y.Z.postman_collection.json: The Postman collection that matches the current API version.

## Enviroment
The application is meant to be run as a Docker container. In order to configure the container the following environment variables
cab be used:
- SECRET_KEY: Flask secret used for cookies signing among others
- FLASK_ENV: The environment where the app is deployed. Typical values are: DEV, STAG, PROD, etc...
- FLASK_APP: This value is hardcoded inside the Docker image to be *app/wsgi.py*
- FLASK_DEBUG
- SQLALCHEMY_DATABASE_URI: Database URI. This application is meant to be used with a MSSQL database, so this URI would be likely similar to this one:  
```mssql+pyodbc://<USER>:<PASSWORD>@<DB_HOST>/<DB>?driver=ODBC+Driver+17+for+SQL+Server```  
Keep in mind that the above example works only for SQL authentication. ODBC driver MUST be in place before running the application.  
For more information about the ODBC driver check out this [link](https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15)
- SQLALCHEMY_ECHO: Turns on/off the SQL output
- APP_LOG_LEVEL: Application-wise log level
