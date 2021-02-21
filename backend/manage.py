from flask_script import Manager

from api import app
from commands.seed_command import SeedCommand


manager = Manager(app)
app.app_context().push()
manager.add_command("seed_db", SeedCommand)


@manager.command
def run():
    app.run()


if __name__ == "__main__":
    manager.run()
