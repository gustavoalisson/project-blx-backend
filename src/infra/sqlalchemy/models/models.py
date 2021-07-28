from sqlalchemy import Column, Integer, String, Float, Boolean
from src.infra.sqlalchemy.config.database import Base

# REPRESENTAÇÕES DA TABELA DO BD
class Product(Base):
    
    __tablename__ = 'produto'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    details = Column(String)
    price = Column(Float)
    status = Column(Boolean)
    