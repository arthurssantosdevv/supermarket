from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CaixaBase(BaseModel):
    nome: Optional[str] = None
    aberto_por: int

class CaixaCreate(CaixaBase):
    pass

class CaixaResponse(CaixaBase):
    id: int
    aberto_em: Optional[datetime]
    fechado_em: Optional[datetime]
    class Config:
        from_attributes = True