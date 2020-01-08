# coding=utf-8
import os

from sqlalchemy.orm import sessionmaker

from .models import Base
from sqlalchemy import create_engine

__author__ = 'anh.dv'

__database_uri = os.getenv('DATABASE_URI')
engine = create_engine(__database_uri)
Session = sessionmaker(bind=engine)
session = Session()

