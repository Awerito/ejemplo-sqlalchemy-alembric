from sqlalchemy import Column, Integer, String
from .db import Base


class Cuenta(Base):
    __tablename__ = "cuenta"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    saldo = Column(Integer, nullable=False)


class Transaccion(Base):
    __tablename__ = "transaccion"
    id = Column(Integer, primary_key=True)
    cuenta_id = Column(Integer, nullable=False)
    monto = Column(Integer, nullable=False)
    tipo = Column(String, nullable=False)  # 'ingreso' o 'gasto'
    descripcion = Column(String, nullable=True)
