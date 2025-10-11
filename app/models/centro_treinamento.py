from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class CentroTreinamento(Base):
    __tablename__ = "centros"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False, unique=True)
    endereco = Column(String(255), nullable=True)

    atletas = relationship("Atleta", back_populates="centro", cascade="all, delete-orphan")
