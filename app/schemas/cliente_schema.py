from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class ClienteBase(BaseModel):
    nome: str
    cpf: Optional[str] = None
    telefone: Optional[str] = None
    email: Optional[EmailStr] = None

class ClienteCreate(ClienteBase):
    senha: str

class ClienteResponse(ClienteBase):
    id: int
    criado_em: datetime
    class Config:
        from_attributes = True