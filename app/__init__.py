import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import config

db = SQLAlchemy()

def create_app(environment="dev"):
    app = Flask(__name__)

    config_map = {
        'dev': config.Development(),
        'test': config.Testing(),
        'prod': config.Production(),
    }
    config_obj = config_map[environment.lower()]

    app.config.from_object(config_obj)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
 
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
