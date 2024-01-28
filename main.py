from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.product_controller import routerProduct

app = FastAPI()

origins = [
   "*"
]

app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials = True,
   allow_methods=["*"],
   allow_headers=["*"]
)

@app.get("/")
def read_root():
   return { "llave":"prueba" }

app.include_router(routerProduct)