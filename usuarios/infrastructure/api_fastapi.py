from fastapi import FastAPI, HTTPException
from application.servicios import UsuarioService
from infrastructure.repository_sqlite import SQLiteRepository
from domain.usuario import Usuario

app = FastAPI()

# Inyección de dependencias manual
repositorio = SQLiteRepository()
servicio = UsuarioService(repositorio)

@app.post("/usuarios/")
def crear_usuario(usuario: Usuario):
    return servicio.registrar_usuario(usuario.id_usuario, usuario.nombre, usuario.email)

@app.get("/usuarios/{id_usuario}")
def leer_usuario(id_usuario: int):
    usuario = servicio.obtener_usuario(id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@app.put("/usuarios/{id_usuario}")
def actualizar_usuario(id_usuario: int, nombre: str, email: str):
    return servicio.modificar_usuario(id_usuario, nombre, email)

@app.delete("/usuarios/{id_usuario}")
def eliminar_usuario(id_usuario: int):
    return servicio.borrar_usuario(id_usuario)

# Para correr: uvicorn infrastructure.api_fastapi:app --port 8001
