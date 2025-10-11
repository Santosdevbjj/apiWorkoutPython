from pydantic import BaseModel, constr, Field

class AtletaBase(BaseModel):
    nome: str = Field(..., example="João Silva")
    cpf: constr(min_length=11, max_length=20) = Field(..., example="12345678901")

class AtletaCreate(AtletaBase):
    categoria_id: int | None = Field(None, example=1)
    centro_id: int | None = Field(None, example=1)

class AtletaRead(AtletaBase):
    id: int
    categoria: str | None = None
    centro_treinamento: str | None = None

    class Config:
        from_attributes = True
        orm_mode = True
