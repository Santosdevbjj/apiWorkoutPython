# Exemplo em src/api/v1/rotas/atleta.py

@router.get(
    '/', 
    summary='Consultar todos os Atletas',
    status_code=status.HTTP_200_OK,
    response_model=Page[AtletaGetCustomizado]  # Usa paginação e schema customizado
)
async def consultar_atletas(
    db_session: DatabaseDependency,
    nome: Optional[str] = Query(None, description='Filtrar por nome do atleta'),
    cpf: Optional[str] = Query(None, description='Filtrar por CPF do atleta'),
    params: Params = Depends() # Dependência da fastapi_pagination
) -> Page[AtletaGetCustomizado]:
    # Lógica para construir a query com base nos filtros (nome e cpf)
    # ...
    # Retorna o resultado paginado
    # return paginate(query, params)
