# product_api
Simple REST API in Python, built with Flask.

## Packages used
* Flask
* Flask-sqlalchemy
* marshmallow

    and other minor ones
    
## Usage
1. Clone the repository
2. Open terminal/cmd in dir
3. Install virtualenv
    ~~~sh
    > pip install virtualenv
    ~~~
4. Create and activate a new virtual environment
    ~~~sh
    # Windows
    > python -m venv venv
    > venv\Scripts\activate
    ~~~
5. Install requirements
    ~~~sh
    > pip install -r requirements.txt
    ~~~
6. Set environment variables
    ~~~sh
    > set FLASK_APP=app:create_app("dev")
    > set FLASK_ENV=development
    ~~~
7. Run
    * a. Tests
        ~~~sh
        > python -m unittest discover
        ~~~
    * b. Application
        ~~~sh
        > flask init-db [--seed] # first init DB and seed it if wanted
        > flask run
        ~~~

## API Schema
### **Product**

|Method| Route       | Description
|-|-|-|
| GET    | /api/v1/product                              | Get all products
| GET    | /api/v1/product/< productid >                | Get a single product by id
| GET    | /api/v1/product/category/< categoryid >      | Get all products in category
| POST   | /api/v1/product/category/                    | Add new product
| PUT    | /api/v1/product/< productid >                | Edit existing product by id
| DELETE | /api/v1/product/< productid >                | Delete existing product by id

### **Productcategory**

|Method| Route       | Description
|-|-|-|
| GET    | /api/v1/productcategory                         | Get all productcategories
| GET    | /api/v1/productcategory/< productid >           | Get a single productcategory by id
| POST   | /api/v1/productcategory/                        | Add new productcategory
| PUT    | /api/v1/productcategory/< productcategory >     | Edit existing productcategory by id
| DELETE | /api/v1/productcategory/< productcategoryid >   |Delete existing productcategory by id

## Unittest coverage
~~~sh
Name                                    Stmts   Miss  Cover
-----------------------------------------------------------
app\__init__.py                            21      0   100%
app\api\product.py                         59      6    90%
app\api\productcategory.py                 47      4    91%
app\config.py                              12      0   100%
app\db_init.py                             34     13    62%
app\models\product.py                      10      1    90%
app\models\productcategory.py               5      0   100%
app\schemas\product_schema.py              11      0   100%
app\schemas\productcategory_schema.py       9      0   100%
test\__init__.py                            0      0   100%
test\test_product.py                       46      1    98%
test\test_product_in_category.py           31      1    97%
test\test_productcategory.py               46      1    98%
-----------------------------------------------------------
TOTAL                                     331     27    92%
~~~