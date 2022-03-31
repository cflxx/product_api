from app.models.productcategory import ProductCategory
from marshmallow import Schema, fields, post_load, validate


class ProductCategorySchema(Schema):
    id = fields.Integer()
    name = fields.String(required=True, validate=validate.Length(min=1, max=64))

    @post_load
    def make_object(self, data):
        return ProductCategory(**data)


productcategory_schema = ProductCategorySchema()
