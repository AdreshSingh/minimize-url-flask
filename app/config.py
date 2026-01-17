import os

class Config:
    SECRET_KEY = "thisisaverysecuritykeyfornowbutitshouldbeshown"
    SQLALCHEMY_DATABASE_URI = "sqlite:///default.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = "jwt-super-secret-key"
