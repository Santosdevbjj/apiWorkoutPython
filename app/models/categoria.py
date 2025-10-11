from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(120), nullable=False, unique=True)
    descricao = Column(String(255), nullable=True)

    atletas = relationship("Atleta", back_populates="categoria", cascade="all, delete-orphan")
