from sqlalchemy.orm import Session

from ..models import Autor


def create_autor(session: Session, nombre: str):
    autor = Autor(nombre=nombre)
    session.add(autor)
    session.commit()
    return autor


def get_autores(session: Session):
    return session.query(Autor).all()


def get_autor(session: Session, autor_id: int):
    return session.get(Autor, autor_id)


def update_autor(session: Session, autor_id: int, nombre: str):
    autor = session.get(Autor, autor_id)
    if autor:
        autor.nombre = nombre
        session.commit()
    return autor


def delete_autor(session: Session, autor_id: int):
    autor = session.get(Autor, autor_id)
    if autor:
        session.delete(autor)
        session.commit()
        return autor
    return None
