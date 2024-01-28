from fastapi import APIRouter
from fastapi.responses import JSONResponse
from application.product_application import get_all_products

routerProduct = APIRouter()
routerProduct.prefix = "/api"

@routerProduct.get("/products")
def list_products():
   result = get_all_products()
   return JSONResponse(content=result)

