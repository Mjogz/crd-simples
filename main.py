from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir que o HTML acesse a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # qualquer origem (apenas para aprendizado)
    allow_methods=["*"],
    allow_headers=["*"],
)

# Lista de usuários em memória
usuarios = []

# Modelo de usuário
class Usuario(BaseModel):
    id: int
    nome: str
    idade: int

# Rota GET - listar usuários
@app.get("/usuarios")
def listar_usuarios():
    return usuarios

# Rota POST - criar usuário
@app.post("/usuarios")
def criar_usuario(usuario: Usuario):
    usuarios.append(usuario)
    return {"mensagem": "Usuário criado com sucesso!", "usuario": usuario}

# Rota DELETE - remove o usuário pelo ID
@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: int):
    for usuario in usuarios:
        if usuario.id == usuario_id:
            usuarios.remove(usuario)
            return {"mensagem": "Usuário removido com sucesso!"}
    return {"mensagem": "Usuário não encontrado"}
