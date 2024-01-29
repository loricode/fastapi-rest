from pydantic import BaseModel

class ProductId(BaseModel):
   id:str

class Product(BaseModel):
   name:str
   price:int
   description:str
