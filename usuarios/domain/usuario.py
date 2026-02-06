from pydantic import BaseModel

class Usuario(BaseModel):
    id_usuario: int
    nombre: str
    email: str