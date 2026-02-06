from fastapi import FastAPI, HTTPException
from domain.pedido import Pedido
from domain.pedido_repository import PedidoRepository
from application.servicios import PedidoService
from typing import List, Optional

app = FastAPI()

# Implementación rápida del repositorio en este mismo archivo para no complicarte
db_pedidos = []

class MemoriaRepo(PedidoRepository):
    def guardar(self, pedido: Pedido):
        db_pedidos.append(pedido)
        return pedido
    
    def buscar_por_id(self, id_pedido: int) -> Optional[Pedido]:
        return next((p for p in db_pedidos if p.id_pedido == id_pedido), None)
    
    def eliminar(self, id_pedido: int):
        global db_pedidos
        db_pedidos = [p for p in db_pedidos if p.id_pedido != id_pedido]
        return {"mensaje": "Pedido eliminado"}

servicio = PedidoService(MemoriaRepo())

@app.post("/pedidos/")
def crear(pedido: Pedido):
    return servicio.crear_pedido(pedido.id_pedido, pedido.detalle, pedido.id_usuario)

@app.get("/pedidos/{id_pedido}")
def leer(id_pedido: int):
    res = servicio.obtener_pedido(id_pedido)
    if not res:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return res

@app.delete("/pedidos/{id_pedido}")
def borrar(id_pedido: int):
    return servicio.borrar_pedido(id_pedido)