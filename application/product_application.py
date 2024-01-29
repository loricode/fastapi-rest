from persistence.product_persistence import  get_productDB, get_all_productsDB, insert_productDB
from models.product import Product
import json

def get_all_products():

   myCursor = get_all_productsDB()
   result = list(myCursor)
   serializables = json.loads(json.dumps(result, default=str))
   return serializables

def insert_product(product:Product):

   product_dict = dict(product)
   json_data = json.loads(json.dumps(product_dict, default=str))
   id_product = insert_productDB(json_data)
   return id_product


def get_product(product_id:str):
   result = get_productDB(product_id)
   product_dict = dict(result)
   json_data = json.loads(json.dumps(product_dict, default=str))
   return json_data