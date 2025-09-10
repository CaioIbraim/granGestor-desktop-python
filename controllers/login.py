from db.database import SessionLocal
from db.models import Usuario

def autenticar_usuario(username, senha):
    db = SessionLocal()
    user = db.query(Usuario).filter_by(username=username, senha=senha).first()
    db.close()
    return user is not None