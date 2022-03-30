from app import db
from marshmallow import fields, Schema, validate, post_load


class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=64))
    description = fields.Str(required=True, validate=validate.Length(min=1, max=128))
    category_id = fields.Int()

    @post_load
    def make_object(self, data):
        return Product(**data)

product_schema = ProductSchema()

class Product(db.Model):

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.relationship("ProductCategory", backref=db.backref("productcategories", lazy="dynamic"))
    category_id = db.Column(db.Integer, db.ForeignKey('productcategories.id'),
    nullable=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(128), nullable=False)

    def serialize(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

