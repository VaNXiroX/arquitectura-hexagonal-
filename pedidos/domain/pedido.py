from pydantic import BaseModel

class Pedido(BaseModel):
    id_pedido: int
    detalle: str      # Ej: "Pizza Doble"
    id_usuario: int   # Relación con el usuario