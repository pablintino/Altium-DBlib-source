import pytest
from app import db, create_app
from tests import setup_db, teardown_db, clean_db


class TestConfig:
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://testuser:Testing12345!@127.0.0.1,1433/altium_db_test?driver=ODBC+Driver+17+for+SQL+Server'
    REDIS_URL = 'redis://'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


@pytest.fixture(scope="session")
def app():
    yield create_app(config_class=TestConfig)


@pytest.fixture(scope="session")
def database(app):
    assert app is not None
    setup_db(app)
    yield db
    teardown_db()


@pytest.fixture(scope="function")
def db_session(database, app):
    assert app is not None
    with app.app_context():
        clean_db()
        yield database.session
        database.session.rollback()
