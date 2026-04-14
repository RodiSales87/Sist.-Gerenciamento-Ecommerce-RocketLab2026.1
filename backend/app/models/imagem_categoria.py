from sqlalchemy import Column, String
from app.database import Base

class CategoriaImagem(Base):
    __tablename__ = "categorias_imagens"
    
    categoria_produto = Column(String(100), primary_key=True)
    link_imagem = Column(String(500), nullable=False)