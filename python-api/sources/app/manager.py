from flask_migrate import Manager, MigrateCommand
from app import create_app

app = create_app()
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
