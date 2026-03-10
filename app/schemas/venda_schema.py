from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class VendaBase(BaseModel):
    cliente_id: Optional[int] = None
    funcionario_id: int
    caixa_id: int
    total: float
    desconto: float = 0

class VendaCreate(VendaBase):
    pass

class VendaResponse(VendaBase):
    id: int
    data_venda: datetime
    class Config:
        from_attributes = True