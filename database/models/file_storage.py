# coding=utf-8
from enum import Enum

from sqlalchemy import Index, Column, BigInteger, String, ForeignKey, Integer
from . import Base

__author__ = 'anh.dv'


class FileStorage(Base):
    __tablename__ = 'file_storage'

    __table_args__ = (
        Index('id', 'id'),
        Index('storage_type', 'storage_type'),
        Index('person_id', 'person_id'),
        Index('replacement_name', 'replacement_name'),
        Index('original_name', 'original_name'),
        Index('extension', 'extension'),
    )

    class StorageType(Enum):
        LOCAL_STORAGE = 'local_storage'
        GOOGLE_CLOUD_STORAGE = 'gcs'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    storage_type = Column(String(50))
    person_id = Column(Integer)
    path = Column(String(255))
    original_name = Column(String(150))
    replacement_name = Column(String(150))
    content_type = Column(String(255))
    extension = Column(String(50))

    def __repr__(self):
        return f'<FileStorage {self.id}>'
