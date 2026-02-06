from abc import ABC, abstractmethod
from .pedido import Pedido
from typing import List, Optional

class PedidoRepository(ABC):
    @abstractmethod
    def guardar(self, pedido: Pedido): pass

    @abstractmethod
    def buscar_por_id(self, id_pedido: int) -> Optional[Pedido]: pass

    @abstractmethod
    def eliminar(self, id_pedido: int): pass