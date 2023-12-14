from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config(object):
    DEBUG = getenv("DEBUG")
    SECRET_KEY = getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI")
