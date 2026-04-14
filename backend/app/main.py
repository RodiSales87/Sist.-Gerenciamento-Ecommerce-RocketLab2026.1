from fastapi import FastAPI
from app.routers import produtos
from app.routers import consumidores
from app.routers import vendedores
from app.routers import pedidos
from app.routers import itens_pedidos
from app.routers import avaliacoes_pedidos
from app.routers import categorias_imagens

app = FastAPI(
    title="Sistema de Compras Online",
    description="API para gerenciamento de pedidos, produtos, consumidores e vendedores.",
    version="1.0.0",
)

@app.get("/", tags=["Health"])
def health_check():
    return {"status": "ok", "message": "API rodando com sucesso!"}

app.include_router(produtos.router)
app.include_router(consumidores.router)
app.include_router(vendedores.router)
app.include_router(pedidos.router)
app.include_router(itens_pedidos.router)
app.include_router(avaliacoes_pedidos.router)
app.include_router(categorias_imagens.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
