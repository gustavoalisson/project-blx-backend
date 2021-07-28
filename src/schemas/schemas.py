from pydantic import BaseModel
from typing import Optional, List

# Classes de modelo = classes que estão representando o negócio
class User(BaseModel):
    id: Optional[str] = None
    name: str
    phone: str
    my_products: List[Product]
    my_sales: List[Solicitation]
    my_solicitations: List[Solicitation]

    class Config:
        orm_mode = True

class Product(BaseModel):
    id: Optional[str] = None
    user: User
    name: str
    details: str
    price: float
    status: bool = False

class Solicitation(BaseModel):
    id: Optional[str] = None
    user: User
    product: Product
    qtd: int
    delivery: bool = True
    address: str
    observation: Optional[str] = "Sem observações"
    

    

    
    
        