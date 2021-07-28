from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemas.schemas import Product
from src.infra.sqlalchemy.repositories.product import RepositoryProduct

app = FastAPI()

@app.post('/products')
def create_product(product: Product, db: Session):
    product_created = RepositoryProduct()._creat(product)
    return {"Message": "Produto criado"}

@app.get('/products')
def list_products():
    return {"Message": "Listagem de produtos"}