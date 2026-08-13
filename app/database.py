from sqlmodel import create_engine, Session, SQLModel
from pathlib import Path
from dotenv import load_dotenv
import os

# 1. Carrega as variáveis de ambiente do arquivo .env
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# 2. Puxa a string de conexão do banco de dados
DATABASE_URL = os.getenv("DATABASE_URL")

# Segurança: Garante que o sistema não vai subir se o .env estiver errado ou ausente
if not DATABASE_URL:
    raise ValueError("A variável de ambiente DATABASE_URL não foi encontrada no arquivo .env")

# 3. O Engine (O Motor)
# echo=True faz com que o SQLModel mostre no terminal o código SQL que ele está gerando. 
# Isso é fantástico para a sua apresentação técnica!
engine = create_engine(DATABASE_URL, echo=True)

# 4. Função para criar as tabelas (A mágica da automação)
def create_db_and_tables():
    # Ele olha para todos os modelos que herdam de SQLModel (como o nosso User)
    # e cria as tabelas no banco de dados se elas não existirem.
    SQLModel.metadata.create_all(engine)

# 5. Dependência para as rotas (A "Sessão" de conversa)
def get_session():
    with Session(engine) as session:
        yield session

print("URL do banco carregada:", DATABASE_URL)