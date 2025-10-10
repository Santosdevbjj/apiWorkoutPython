# Exemplo em src/schemas/atleta.py

class AtletaGetCustomizado(BaseSchema):
    nome: str = Field(description='Nome do atleta')
    centro_treinamento: str = Field(description='Nome do Centro de Treinamento')
    categoria: str = Field(description='Nome da Categoria')

    # Configuração Pydantic (ou usando o .model_validate() no endpoint) para 
    # mapear os dados do Model ORM para este Schema
