import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
 
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI="sqlite:///" + app.instance_path + "/db.sqlite",
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    # SQLAlchemy init
    db.init_app(app)

    # table creation / seeding
    from .db_init import init_db_command
    app.cli.add_command(init_db_command)

    # routes
    from .api import product, productcategory
    app.register_blueprint(product.bp)
    app.register_blueprint(productcategory.bp)
    
    return app
