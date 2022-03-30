from app import db


class ProductCategory(db.Model):

    __tablename__ = "productcategories"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
