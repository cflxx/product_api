from app.models.product import Product
from marshmallow import Schema, fields, post_load, validate


class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=64))
    description = fields.Str(required=True, validate=validate.Length(min=1, max=128))
    category_id = fields.Int()

    @post_load
    def make_object(self, data):
        return Product(**data)

product_schema = ProductSchema()
