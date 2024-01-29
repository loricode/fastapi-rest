from fastapi import APIRouter
from fastapi.responses import JSONResponse
from application.product_application import get_all_products
from models.product import Product, ProductId
from application.product_application import get_product, insert_product

routerProduct = APIRouter()
routerProduct.prefix = "/api"

@routerProduct.get("/products")
def list_products():
   result = get_all_products()
   return JSONResponse(content=result)

@routerProduct.post("/product/get")
def get_one_products(product:ProductId):
   result = get_product(product.id)
   return result

@routerProduct.post("/product/add")
def add_products(product:Product):
   result = insert_product(product)
   return result

