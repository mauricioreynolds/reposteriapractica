from reposteria.database import PkModel, Column, db

class Categoria(PkModel):
    __tablename__ = "categorias"

    nombre = Column(db.String(100), nullable=False, unique=True)
    descripcion = Column(db.String(255), nullable=True)

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

