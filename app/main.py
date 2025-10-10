from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination
from sqlalchemy.exc import IntegrityError

from app.api.v1 import routes_atletas, routes_categorias, routes_centros
from app.exceptions.handlers import integrity_error_handler

app = FastAPI(title="WorkoutAPI", version="0.1.0", description="API de competição de crossfit")

# CORS (ajuste permissões conforme sua política)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(routes_atletas.router)
app.include_router(routes_categorias.router)
app.include_router(routes_centros.router)

# Exception handlers
app.add_exception_handler(IntegrityError, integrity_error_handler)

# FastAPI-pagination
add_pagination(app)
