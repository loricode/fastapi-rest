from fastapi import HTTPException
from config.connection import conn

def get_all_productsDB():

   try:
     return conn.local.products.find()
   except Exception as ints:
    raise HTTPException(status_code=500, detail={"type":ints.__doc__,
                                                 "error":ints.args })