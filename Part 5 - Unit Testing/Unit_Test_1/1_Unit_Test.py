#################################################
#This python file contains
#- Function under development
#- Function to test
#################################################
products = [
    {"id": 1, "name": "Product 1", "price": 10, "description": "Description 1"},
    {"id": 2, "name": "Product 2", "price": 20, "description": "Description 2"},
    {"id": 3, "name": "Product 3", "price": 30, "description": "Description 3"},
]

def test_get_products():
    product = next((p for p in products if p['id'] == 4), None)
    if product:
        assert True
    else:
        assert False


def func(x):
    return x + 1
	
def test_answer():

