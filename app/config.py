class Development(object):
    SECRET_KEY = "dev"
    SQLALCHEMY_DATABASE_URI="sqlite:///../instance/devdb.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class Testing(object):
    SECRET_KEY="test"
    SQLALCHEMY_DATABASE_URI="sqlite:///../instance/testdb.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class Production(object):
    SECRET_KEY="prod"
    SQLALCHEMY_DATABASE_URI="sqlite:///../instance/proddb.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
