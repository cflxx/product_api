from unittest import TestCase
import json
import os
from app import create_app, db
from app.models.product import Product

class ProductInCategoryTest(TestCase):
    """Test product API"""

    def setUp(self):
        self.app = create_app('test')
        self.client = self.app.test_client()
        db.create_all(app=self.app)

    def tearDown(self):
        db.session.remove()
        db.drop_all(app=self.app)

    def test_get_all_products_in_category(self):
        """Test getting all products"""
        res = self.client.post('/api/v1/productcategory/', json=dict(name='testproductcategory1'))

        productcategory1 = json.loads(res.get_data(as_text=True))

        res = self.client.post('/api/v1/productcategory/', json=dict(name='testproductcategory2'))

        productcategory2 = json.loads(res.get_data(as_text=True))

        self.client.post('/api/v1/product/',\
             json=dict(name='testproduct1', 
                       description='testproduct1 desc',
                       category_id=str(productcategory1.get('id'))))

        self.client.post('/api/v1/product/',\
             json=dict(name='testproduct2', 
                       description='testproduct2 desc',
                       category_id=str(productcategory2.get('id'))))

        res = self.client.get('/api/v1/product/category/' + str(productcategory1.get('id')))

        self.assertEqual(res.status_code, 200)
        self.assertIn('testproduct1', str(res.data))

        res = self.client.get('/api/v1/product/category/' + str(productcategory2.get('id')))

        self.assertEqual(res.status_code, 200)
        self.assertIn('testproduct2', str(res.data))

    def test_add_product_to_nonexistent_category(self):
        res = self.client.post('/api/v1/product/',\
             json=dict(name='testproduct2', 
                       description='testproduct2 desc',
                       category_id=-1))
    
        self.assertEqual(res.status_code, 400)


if __name__ == "__main__":
    unittest.main()
