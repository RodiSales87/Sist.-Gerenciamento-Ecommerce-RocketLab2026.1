from typing import Optional
from pydantic import BaseModel

class CategoriaImagemBase(BaseModel):
    link_imagem: str

class CategoriaImagemCreate(CategoriaImagemBase):
    categoria_produto: str

class CategoriaImagemUpdate(BaseModel):
    link_imagem: Optional[str] = None

class CategoriaImagemResponse(CategoriaImagemBase):
    categoria_produto: str

    class Config:
        from_attributes = True
