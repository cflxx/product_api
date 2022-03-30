from app import db
from marshmallow import Schema, fields, validate, post_load


class ProductCategorySchema(Schema):
    id = fields.Integer()
    name = fields.String(required=True, validate=validate.Length(min=1, max=64))

    @post_load
    def make_object(self, data):
        return ProductCategory(**data)


productcategory_schema = ProductCategorySchema()

class ProductCategory(db.Model):

    __tablename__ = "productcategories"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
