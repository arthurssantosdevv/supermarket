from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class FuncionarioBase(BaseModel):
    nome: str
    cargo: Optional[str] = None
    email: EmailStr
    ativo: bool = True

class FuncionarioCreate(FuncionarioBase):
    senha: str

class FuncionarioResponse(FuncionarioBase):
    id: int
    criado_em: datetime
    class Config:
        from_attributes = True