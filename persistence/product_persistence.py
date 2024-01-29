from fastapi import HTTPException
from config.connection import conn
from bson import ObjectId

def get_all_productsDB():

   try:
     return conn.local.products.find()
   except Exception as ints:
    raise HTTPException(status_code=500, detail={"type":ints.__doc__,
                                                 "error":ints.args })
def insert_productDB(product):

  try:
    result = conn.local.products.insert_one(product)
    return str(result.inserted_id)
  except Exception as ints:
   raise HTTPException(status_code=500, detail={"type":ints.__doc__,
                                                "error":ints.args })
  
def get_productDB(product_id):

  try:
    query = {"_id": ObjectId(product_id)}
    result = conn.local.products.find_one(query)
    return result
  except Exception as ints:
   raise HTTPException(status_code=500, detail={"type":ints.__doc__,
                                                "error":ints.args })  