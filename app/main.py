from fastapi import FastAPI
from app.routes.produtos_routes import produto_router

app = FastAPI(
    title="Supermarket PDV API",
    description="API de sistema de checkout de supermercado",
    version="1.0.0")

@app.get("/")
def root():
    return {"message": "API do sistema PDV funcionando"}

app.include_router(produto_router)