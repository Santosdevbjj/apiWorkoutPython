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


    

from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

# ... código da rota POST ...

    try:
        # Lógica para persistir o Atleta no banco de dados
        await db_session.commit()
    except IntegrityError:
        # Lógica para tratar o erro de CPF duplicado
        raise HTTPException(
            status_code=status.HTTP_303_SEE_OTHER, # 303 See Other
            detail=f'Já existe um atleta cadastrado com o cpf: {atleta_in.cpf}'
        )
    except Exception:
        

