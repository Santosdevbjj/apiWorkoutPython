from fastapi import APIRouter

router = APIRouter(prefix="/v1/categorias", tags=["Categorias"])

@router.get("/")
async def list_categorias():
    return {"message": "Lista de categorias - implemente conforme necessário"}
