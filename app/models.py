import uuid
from sqlmodel import Field, SQLModel

# Esta classe representa tanto a TABELA no banco quanto o SCHEMA da API
class User(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4, # Gera um ID novo automaticamente se não enviarmos um
        primary_key=True, 
        index=True,
        nullable=False
    )
    name: str
    email: str = Field(unique=True, index=True) # Garante que não existam dois e-mails iguais