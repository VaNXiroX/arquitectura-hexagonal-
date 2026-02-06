from domain.pedido import Pedido
from domain.pedido_repository import PedidoRepository

class PedidoService:
    def __init__(self, repositorio: PedidoRepository):
        self.repositorio = repositorio

    def crear_pedido(self, id_pedido: int, detalle: str, id_usuario: int):
        nuevo = Pedido(id_pedido=id_pedido, detalle=detalle, id_usuario=id_usuario)
        return self.repositorio.guardar(nuevo)

    def obtener_pedido(self, id_pedido: int):
        return self.repositorio.buscar_por_id(id_pedido)

    def borrar_pedido(self, id_pedido: int):
        return self.repositorio.eliminar(id_pedido)