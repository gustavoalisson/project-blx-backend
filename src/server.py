from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemas.schemas import Product
from src.infra.sqlalchemy.config.database import get_db, creat_db
from src.infra.sqlalchemy.repositories.product import RepositoryProduct

creat_db()

app = FastAPI()

@app.post('/products')
def create_product(product: Product, db: Session = Depends(get_db)):
    product_created = RepositoryProduct(db)._creat(product)
    return product_created

@app.get('/products')
def list_products():
    return {"Message": "Listagem de produtos"}