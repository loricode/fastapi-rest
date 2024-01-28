from persistence.product_persistence import get_all_productsDB
import json

def get_all_products():

   myCursor = get_all_productsDB()
   result = list(myCursor)
   serializables = json.loads(json.dumps(result, default=str))
   return serializables