from pydantic import BaseModel, Field

class CentroCreate(BaseModel):
    nome: str = Field(..., example="CrossFit Central")
    endereco: str | None = Field(None, example="Rua Exemplo, 123")

class CentroRead(CentroCreate):
    id: int

    class Config:
        orm_mode = True
