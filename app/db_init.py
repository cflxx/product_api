from sqlite3 import Connection as SQLite3Connection

import click
from flask import current_app, g
from flask.cli import with_appcontext
from sqlalchemy import event
from sqlalchemy.engine import Engine

from . import db
from .models.product import Product
from .models.productcategory import ProductCategory


@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    """
    Force sqlite to enforce foreign keys, as it doesn't by default
    Source: https://stackoverflow.com/a/15542046
    """
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

def create_db():
    db.drop_all()
    db.create_all()

def seed_db():
    db.session.add(ProductCategory(id=1, name="productcategory1"))
    db.session.add(ProductCategory(id=2, name="productcategory2"))
    db.session.add(ProductCategory(id=3, name="productcategory3"))
    db.session.add(Product(name="product1", description="product1 description", category_id=1))
    db.session.add(Product(name="product2", description="product2 description", category_id=2))
    db.session.add(Product(name="product3", description="product3 description", category_id=3))
    db.session.commit()


@click.command('init-db')
@click.option("--seed", is_flag=True, show_default=True,\
         default=False, help="Seed db with initial data.")
@with_appcontext
def init_db_command(seed):
    """Clear the existing data and create new tables."""
    create_db()

    if seed:
        seed_db()

    click.echo('Initialized the database.')
