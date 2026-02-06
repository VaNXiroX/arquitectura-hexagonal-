from domain.usuario import Usuario
from domain.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self, repositorio: UsuarioRepository):
        self.repositorio = repositorio

    def registrar_usuario(self, id_usuario: int, nombre: str, email: str):
        nuevo_usuario = Usuario(id_usuario=id_usuario, nombre=nombre, email=email)
        return self.repositorio.guardar(nuevo_usuario)

    def obtener_usuario(self, id_usuario: int):
        return self.repositorio.buscar_por_id(id_usuario)
    
    def listar_usuarios(self):
        return self.repositorio.listar_todos()

    def modificar_usuario(self, id_usuario: int, nombre: str, email: str):
        return self.repositorio.actualizar(id_usuario, nombre, email)

    def borrar_usuario(self, id_usuario: int):
        return self.repositorio.eliminar(id_usuario)