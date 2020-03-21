import sqlite3
from sqlite3 import Error
from argparse import ArgumentParser
from app import db


class SQliteDatabse(object):

    def __init__(self, file_name):
        self._file_name = file_name
        self._connection = None

    def create_database(self):

        try:
            self._connection = sqlite3.connect(self._file_name)
            return True
        except Error as e:
            print(e)
        finally:
            if self._connection:
                self._connection.close()

            db.create_all()



if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-d", "--database", help="""Enter the name of the database or the full path 
                                  to create it in a different directory""", type=str)
    args = parser.parse_args()

    if args.database:
        db = SQliteDatabse(file_name=args.database)
        print("Creating database please wait...")

        if db.create_database():
            print("Successfully created database")
        else:
            print("Failed to create database")