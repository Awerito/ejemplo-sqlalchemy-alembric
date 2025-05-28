from sqlalchemy import Column, Integer, String, ForeignKey, Time
from .db import Base


class EjemploRelacion(Base):
    __tablename__ = "ejemplo_relacion"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    descripcion = Column(String, index=True)
    tiempo = Column(Time, nullable=False)

    # Clave foranea a otro modelo
    otro_id = Column(Integer, ForeignKey("otro_modelo.id"))

    # Relación con otro modelo (descomentar si es necesario)
    # otro_modelo = relationship("OtroModelo", back_populates="ejemplo_relacion")
