import uuid
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from .database import engine, get_session
from .models import User

app = FastAPI(title="Minha API de Usuários")

# Rota para Criar Usuário (POST)
@app.post("/users", response_model=User, status_code=201)
def create_user(user: User, session: Session = Depends(get_session)):
    session.add(user) # Adiciona o usuário na sessão
    session.commit() # Salva no banco de dados
    session.refresh(user) # Atualiza o objeto com o ID gerado
    return user

# Rota para Listar Usuários (GET)
@app.get("/users", response_model=List[User])
def read_users(session: Session = Depends(get_session)):
    users = session.exec(select(User)).all() # Busca todos no banco
    return users

# Essa seria a nova rota para buscar UM usuário específico
@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: uuid.UUID, session: Session = Depends(get_session)):
    # O banco de dados usa o ÍNDICE que discutimos para achar esse ID rápido
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user