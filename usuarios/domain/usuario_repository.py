from abc import ABC, abstractmethod
from .usuario import Usuario
from typing import List, Optional

class UsuarioRepository(ABC):
    @abstractmethod
    def guardar(self, usuario: Usuario): pass

    @abstractmethod
    def buscar_por_id(self, id_usuario: int) -> Optional[Usuario]: pass

    @abstractmethod
    def listar_todos(self) -> List[Usuario]: pass

    @abstractmethod
    def actualizar(self, id_usuario: int, nombre: str, email: str): pass

    @abstractmethod
    def eliminar(self, id_usuario: int): pass