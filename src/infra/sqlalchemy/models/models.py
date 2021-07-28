from sqlalchemy import Column, Integer, String, Float, Boolean
from src.infra.sqlalchemy.config.database import Base

# REPRESENTAÇÕES DA TABELA DO BD
class Product(Base):
    
    __tablename__ = 'produto'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    details = Column(String(500))
    price = Column(Float)
    status = Column(Boolean)
    