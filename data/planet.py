import sqlalchemy
from sqlalchemy import Column, Integer, ForeignKey

from .db_session import SqlAlchemyBase


class Planet(SqlAlchemyBase):
    __tablename__ = 'planet'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
