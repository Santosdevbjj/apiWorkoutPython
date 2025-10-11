from pydantic import BaseModel, Field

class CategoriaCreate(BaseModel):
    nome: str = Field(..., example="Elite")
    descricao: str | None = Field(None, example="Categoria elite masculina")

class CategoriaRead(CategoriaCreate):
    id: int

    class Config:
        orm_mode = True
