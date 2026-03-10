import sqlite3
from fastapi import APIRouter
from app.schemas.produto_schema import ProdutoCreate, ProdutoUpdate
from app.connection import get_connection
from zoneinfo import ZoneInfo
from datetime import datetime

produto_router = APIRouter(prefix="/produtos", tags=["produtos"])
agora = datetime.now(ZoneInfo("America/Sao_Paulo"))

@produto_router.post("/criar-produtos")
def criar_produto(produto: ProdutoCreate):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO produtos (nome, categoria, sku, custo, estoque, ativo, criado_em)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        produto.nome,
        produto.categoria,
        produto.sku,
        produto.custo,
        produto.estoque,
        produto.ativo,
        agora
        
    ))
    
    print(cursor.fetchall())
    conn.commit()
    conn.close()

    return {"message": "Produto criado com sucesso"}

@produto_router.get("/buscar-produtos/{sku}")
def buscar_produto(sku: str):

    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM produtos WHERE sku = ?", (sku,))
    produto = cursor.fetchone()

    conn.close()

    if produto:
        return dict(produto)
    return {"erro": "Produto não encontrado"}

@produto_router.put("/atualizar-produtos/{sku}")
def atualizar_produto(produto: ProdutoUpdate, sku: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE produtos
        SET nome = ?, categoria = ?, custo = ?, estoque = ?, ativo = ?
        WHERE sku = ?
    """, (
        produto.nome,
        produto.categoria,
        produto.custo,
        produto.estoque,
        produto.ativo,
        sku
    ))

    conn.commit()

    if cursor.rowcount == 0:
        return {"erro": "Produto não encontrado"}
    conn.close()

    return {"message": "Produto atualizado com sucesso"}