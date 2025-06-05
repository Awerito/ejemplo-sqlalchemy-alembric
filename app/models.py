from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    Boolean,
    ForeignKey,
    Table,
    ForeignKeyConstraint,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


from .db import Base


# Tablas de asociación para relaciones many-to-many
libro_categoria = Table(
    "libro_categoria",
    Base.metadata,
    Column("libro_id", Integer, ForeignKey("libro.id"), primary_key=True),
    Column("categoria_id", Integer, ForeignKey("categoria.id"), primary_key=True),
)

libro_autor = Table(
    "libro_autor",
    Base.metadata,
    Column("libro_id", Integer, ForeignKey("libro.id"), primary_key=True),
    Column("autor_id", Integer, ForeignKey("autor.id"), primary_key=True),
)


class Autor(Base):
    __tablename__ = "autor"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    libros = relationship("Libro", secondary=libro_autor, back_populates="autores")


class Categoria(Base):
    __tablename__ = "categoria"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    libros = relationship(
        "Libro", secondary=libro_categoria, back_populates="categorias"
    )


class Libro(Base):
    __tablename__ = "libro"
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    publicacion = Column(Date)
    categorias = relationship(
        "Categoria", secondary=libro_categoria, back_populates="libros"
    )
    autores = relationship("Autor", secondary=libro_autor, back_populates="libros")
    prestamos = relationship("Prestamo", back_populates="libro")


class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    correo = Column(String, unique=True, nullable=False)
    registro = Column(Date)
    prestamos = relationship("Prestamo", back_populates="usuario")


class Prestamo(Base):
    __tablename__ = "prestamo"
    usuario_id = Column(Integer, ForeignKey("usuario.id"), primary_key=True)
    libro_id = Column(Integer, ForeignKey("libro.id"), primary_key=True)
    prestamo = Column(Date, server_default=func.now())
    devolucion = Column(Date)
    estado = Column(String)

    usuario = relationship("Usuario", back_populates="prestamos")
    libro = relationship("Libro", back_populates="prestamos")
    multa = relationship("Multa", uselist=False, back_populates="prestamo")


class Multa(Base):
    __tablename__ = "multa"
    id = Column(Integer, primary_key=True, autoincrement=True)
    monto = Column(Integer, nullable=False)
    pagado = Column(Boolean, server_default="FALSE")
    prestamo_usuario_id = Column(Integer)
    prestamo_libro_id = Column(Integer)

    __table_args__ = (
        ForeignKeyConstraint(
            ["prestamo_usuario_id", "prestamo_libro_id"],
            ["prestamo.usuario_id", "prestamo.libro_id"],
        ),
    )

    prestamo = relationship("Prestamo", back_populates="multa")
