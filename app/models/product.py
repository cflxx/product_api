from app import db


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
