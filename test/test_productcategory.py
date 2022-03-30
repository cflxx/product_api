from unittest import TestCase
import os
import json
from app import create_app, db
from app.models.productcategory import ProductCategory

class ProductCategoryTest(TestCase):
    """Test productcategory API"""

    def setUp(self):
        self.app = create_app('test')
        self.client = self.app.test_client()
        db.create_all(app=self.app)

    def tearDown(self):
        db.session.remove()
        db.drop_all(app=self.app)

    def test_add_productcategory(self):
        """Test adding a product"""
        res = self.client.post('/api/v1/productcategory/', json=dict(name='testproductcategory'))

        self.assertEqual(res.status_code, 201)
        self.assertIn('testproductcategory', str(res.data))

    def test_get_all_productcategories(self):
        """Test getting all products"""
        self.client.post('/api/v1/productcategory/', json=dict(name='testproductcategory1'))
        self.client.post('/api/v1/productcategory/', json=dict(name='testproductcategory2'))

        res = self.client.get('/api/v1/productcategory/')

        self.assertEqual(res.status_code, 200)
        self.assertIn('productcategory1', str(res.data))
        self.assertIn('productcategory2', str(res.data))

    def test_get_productcategory_by_id(self):
        """Test getting product by id"""
        res = self.client.post('/api/v1/productcategory/', json=dict(name='testproductcategory1'))
        
        productcategory = json.loads(res.get_data(as_text=True))

        res = self.client.get('/api/v1/productcategory/' + str(productcategory.get('id')))

        self.assertEqual(res.status_code, 200)
        self.assertIn('productcategory1', str(res.data))

    def test_edit_productcategory_by_id(self):
        """Test editing an existing product"""
        res = self.client.post('/api/v1/productcategory/', json=dict(name='testproductcategory1'))
        
        productcategory = json.loads(res.get_data(as_text=True))

        new_productcategory_data = dict(name='testproductcategory3')
        self.client.put('/api/v1/productcategory/' + str(productcategory.get('id')),\
                         json=new_productcategory_data)

        res = self.client.get('/api/v1/productcategory/' + str(productcategory.get('id')))

        self.assertIn('testproductcategory3', str(res.data))

    def test_delete_productcategory_by_id(self):
        """Test deleting an existing product"""
        res = self.client.post('/api/v1/productcategory/', json=dict(name='testproductcategory1'))
        
        productcategory = json.loads(res.get_data(as_text=True))

        res = self.client.delete('/api/v1/productcategory/' + str(productcategory.get('id')))

        self.assertEqual(res.status_code, 200)

        res = self.client.get('/api/v1/productcategory/' + str(productcategory.get('id')))

        self.assertEqual(res.status_code, 404)


if __name__ == "__main__":
    unittest.main()
