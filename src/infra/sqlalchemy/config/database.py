from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# CONFIGURAÇÕES DO BANCO DE DADOS
# ESPECIFICAÇÕES MA DOCUMENTAÇÃO

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://adteste@spV#KJ^sBM!$@10.0.10.39/apenas_teste"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def creat_db():
    Base.metada.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    
        
