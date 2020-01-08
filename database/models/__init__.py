# coding=utf-8
from sqlalchemy.ext.declarative import declarative_base

__author__ = 'anh.dv'

Base = declarative_base()

from .file_storage import FileStorage
