import unittest
import json
from app import create_app, db


class productTest(unittest.TestCase):
    """Test product API"""

    def setUp(self):
        self.app = create_app('test')
        self.client = self.app.test_client()
        db.create_all(app=self.app)

    def tearDown(self):
        db.session.remove()
        db.drop_all(app=self.app)

    def test_add_product(self):
        """Test adding a product"""
        res = self.client.post('/api/v1/product/', \
            json=dict(name='testproduct', description='testproduct desc'))

        self.assertEqual(res.status_code, 201)
        self.assertIn('testproduct', str(res.data))

    def test_get_all_products(self):
        """Test getting all products"""
        self.client.post('/api/v1/product/',\
             json=dict(name='testproduct1', description='testproduct1 desc'))
        self.client.post('/api/v1/product/',\
             json=dict(name='testproduct2', description='testproduct2 desc'))

        res = self.client.get('/api/v1/product/')

        self.assertEqual(res.status_code, 200)
        self.assertIn('testproduct1', str(res.data))
        self.assertIn('testproduct2 desc', str(res.data))
    
    def test_get_product_by_id(self):
        """Test getting product by id"""
        res = self.client.post('/api/v1/product/',\
             json=dict(name='testproduct1', description='testproduct1 desc'))
        
        product = json.loads(res.get_data(as_text=True))

        res = self.client.get('/api/v1/product/' + str(product.get('id')))

        self.assertEqual(res.status_code, 200)
        self.assertIn('testproduct1', str(res.data))

    def test_edit_product_by_id(self):
        """Test editing an existing product"""
        res = self.client.post('/api/v1/product/',\
                json=dict(name='testproduct1', description='testproduct1 desc'))

        product = json.loads(res.get_data(as_text=True))

        new_product_data = dict(name='testproductedited',\
             description='testproductedited desc')

        self.client.put('/api/v1/product/' + str(product.get('id')),\
                         json=new_product_data)

        res = self.client.get('/api/v1/product/' + str(product.get('id')))

        self.assertIn('testproductedited', str(res.data))

    def test_delete_product_by_id(self):
        """Test deleting an existing product"""
        res = self.client.post('/api/v1/product/',\
             json=dict(name='testproduct1', description='testproduct1 desc'))
        
        product = json.loads(res.get_data(as_text=True))

        res = self.client.delete('/api/v1/product/' + str(product.get('id')))

        self.assertEqual(res.status_code, 200)

        res = self.client.get('/api/v1/product/1' + str(product.get('id')))

        self.assertEqual(res.status_code, 404)


if __name__ == "__main__":
    unittest.main()
