from domain.usuario_repository import UsuarioRepository
from domain.usuario import Usuario
from typing import List, Optional

# Simulación en memoria (puede cambiarse por conexión SQLite real aquí mismo)
db_memoria = []

class SQLiteRepository(UsuarioRepository):
    def guardar(self, usuario: Usuario):
        db_memoria.append(usuario)
        return usuario

    def buscar_por_id(self, id_usuario: int) -> Optional[Usuario]:
        return next((u for u in db_memoria if u.id_usuario == id_usuario), None)

    def listar_todos(self) -> List[Usuario]:
        return db_memoria

    def actualizar(self, id_usuario: int, nombre: str, email: str):
        usuario = self.buscar_por_id(id_usuario)
        if usuario:
            usuario.nombre = nombre
            usuario.email = email
            return usuario
        return None

    def eliminar(self, id_usuario: int):
        global db_memoria
        # Filtramos la lista para excluir el ID eliminado
        db_memoria = [u for u in db_memoria if u.id_usuario != id_usuario]
        return {"mensaje": "Usuario eliminado"}