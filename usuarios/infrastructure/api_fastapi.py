from fastapi import FastAPI
from usuarios.application.servicios import UsuarioService
from usuarios.infrastructure.repository_sqlite import SQLiteRepository

app = FastAPI()
repo = SQLiteRepository()
service = UsuarioService(repo)

@app.post("/usuarios/")
def create_user(usuario: dict):
    return service.registrar_usuario(usuario)