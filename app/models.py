from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table, func
from sqlalchemy.orm import relationship


from .db import Base


# Ejemplo de relación uno a uno
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    edad = Column(Integer, nullable=False)

    pasaporte = relationship(
        "Pasaporte", uselist=False, back_populates="usuario"
    )  # Relación uno a uno


class Pasaporte(Base):
    __tablename__ = "pasaportes"
    id = Column(Integer, primary_key=True)
    numero = Column(String)
    fecha_emision = Column(
        DateTime, server_default=func.now()
    )  # Fecha de emisión con valor por defecto fecha y hora actual

    usuario_id = Column(
        Integer, ForeignKey("usuarios.id"), nullable=False, unique=True
    )  # Clave foránea a usuarios.id
    usuario = relationship("Usuario", back_populates="pasaporte")  # Relación uno a uno


# Ejemplo de relación uno a muchos
class Autor(Base):
    __tablename__ = "autores"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    articulos = relationship(
        "Articulo", back_populates="autor"
    )  # Relación uno a muchos


class Articulo(Base):
    __tablename__ = "articulos"
    id = Column(Integer, primary_key=True)
    titulo = Column(String)

    autor_id = Column(Integer, ForeignKey("autores.id"))  # Clave foránea a autores.id
    autor = relationship("Autor", back_populates="articulos")  # Relación uno a muchos


# Ejemplo de relación muchos a muchos
estudiante_curso = Table(
    "estudiante_curso",  # nombre de la tabla intermedia en la base de datos
    Base.metadata,
    Column(
        "estudiante_id", ForeignKey("estudiantes.id"), primary_key=True
    ),  # Clave foránea a estudiantes.id
    Column(
        "curso_id", ForeignKey("cursos.id"), primary_key=True
    ),  # Clave foránea a cursos.id
)  # Tabla intermedia para la relación muchos a muchos


class Estudiante(Base):
    __tablename__ = "estudiantes"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)

    cursos = relationship(
        "Curso", secondary=estudiante_curso, back_populates="estudiantes"
    )  # Relación muchos a muchos con cursos


class Curso(Base):
    __tablename__ = "cursos"
    id = Column(Integer, primary_key=True)
    titulo = Column(String)

    estudiantes = relationship(
        "Estudiante", secondary=estudiante_curso, back_populates="cursos"
    )  # Relación muchos a muchos con estudiantes
