from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositoryProduct():
    def __init__(self, db: Session):
        self.db = db
    
    def _creat(self, product: schemas.Product):
        db_product = models.Product(name = product.name, detais = product.details,
                                    price = product.price, status = product.status)

        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product
    
    def _list(self):
        products = self.db.query(models.Product).all
        return products
    
    def _get(self):
        pass
    
    def remove(self):
        pass