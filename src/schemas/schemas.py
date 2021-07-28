from pydantic import BaseModel
from typing import Optional, List

# Classes de modelo = classes que estão representando o negócio
class User(BaseModel):
    id: Optional[str] = None
    name: str
    phone: str

    class Config:
        orm_mode = True

class Product(BaseModel):
    id: Optional[str] = None
    name: str
    details: str
    price: float
    status: bool = False

class Solicitation(BaseModel):
    id: Optional[str] = None
    qtd: int
    delivery: bool = True
    address: str
    observation: Optional[str] = "Sem observações"
    

    

    
    
        