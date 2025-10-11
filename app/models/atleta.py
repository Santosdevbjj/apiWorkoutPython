from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Atleta(Base):
    __tablename__ = "atletas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    cpf = Column(String(20), nullable=False, unique=True, index=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id", ondelete="SET NULL"), nullable=True)
    centro_id = Column(Integer, ForeignKey("centros.id", ondelete="SET NULL"), nullable=True)

    categoria = relationship("Categoria", back_populates="atletas")
    centro = relationship("CentroTreinamento", back_populates="atletas")
