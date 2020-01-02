from sqlalchemy import Column, String

# local import
from .database import Base


class Config(Base):
    """
    configs table with two columns

    name: str (unique)
    
    metadatac: nested key:value implemented as str
    """

    __tablename__ = "configs"

    name = Column(String, primary_key=True)
    metadatac = Column(String)
