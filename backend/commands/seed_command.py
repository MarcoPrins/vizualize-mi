from flask_script import Command

from load_data import load_data


class SeedCommand(Command):
    """ Seed the DB."""

    def run(self):
        load_data()
