from app import db
from app.models.product import Product
from app.schemas.product_schema import product_schema
from flask import Blueprint, Flask, jsonify, request


bp = Blueprint('product', __name__, url_prefix='/api/v1/product')

@bp.route('/', methods=['GET'])
def get_products():
    """Get all products"""
    product = Product.query.all()
    result = product_schema.dump(product, many=True)

    return {"products" : result.data}

@bp.route('/<int:productid>', methods=['GET'])
def get_product(productid):
    """Get a product by id"""
    product = Product.query.get_or_404(productid)
    result = product_schema.dump(product)

    return result.data

@bp.route('/category/<int:categoryid>', methods=['GET'])
def get_products_in_category(categoryid):
    """Get all products in a category by category id"""
    product = Product.query.filter_by(category_id=categoryid).all()
    result = product_schema.dump(product, many=True)

    return {"products" : result.data}

@bp.route('/', methods=['POST'])
def create_product():
    """Create new product"""
    json_data = request.get_json()

    if not json_data:
        return "No data provided", 404

    # Validate and deserialize input
    deserialize_result = product_schema.load(json_data)
    if (any(deserialize_result.errors)):
        return deserialize_result.errors, 400

    new_product = deserialize_result.data

    db.session.add(new_product)

    # foreign key constraint check
    try:
        db.session.commit()
    except:
        return "Productcategory doesn't exist", 400

    result = product_schema.dump(Product.query.get(new_product.id))
    
    return result.data, 201

@bp.route('/<int:productid>', methods=['PUT'])
def update_product(productid):
    """Update an existing product"""
    product = Product.query.get_or_404(productid)
    json_data = request.get_json()

    if not json_data:
        return "No data provided", 404

    # Validate and deserialize input
    new_product = product_schema.load(json_data)
    if (any(new_product.errors)):
        return new_product.errors

    product.name = new_product.data.name
    product.description = new_product.data.description
    product.category_id = new_product.data.category_id

    # foreign key constraint check
    try:
        db.session.commit()
    except:
        return "Productcategory doesn't exist", 400

    return product_schema.dump(product).data, 201

@bp.route('/<int:productid>', methods=['DELETE'])
def delete_product(productid):
    """Delete a product by id"""
    query = Product.query.get_or_404(productid)

    db.session.delete(query)
    db.session.commit()

    return '', 200
