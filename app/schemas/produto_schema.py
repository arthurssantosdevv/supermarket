from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ProdutoBase(BaseModel):
    nome: str
    categoria: Optional[str] = None
    sku: str
    custo: Optional[float] = None
    estoque: int = 0
    ativo: bool = True

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoResponse(ProdutoBase):
    id: int
    criado_em: datetime
    class Config:
        from_attributes = True
        
class ProdutoUpdate(BaseModel):
    nome: Optional[str] = None
    categoria: Optional[str] = None
    custo: Optional[float] = None
    estoque: Optional[int] = None
    ativo: Optional[bool] = None