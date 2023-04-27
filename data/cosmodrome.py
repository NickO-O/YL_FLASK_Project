import sqlalchemy
from sqlalchemy import Column, Integer, ForeignKey

from .db_session import SqlAlchemyBase


class Cosmodrome(SqlAlchemyBase):
    __tablename__ = 'cosmodrome'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    planet_id = Column(
        Integer,
        ForeignKey('planet.id', ondelete='CASCADE'),
        nullable=False,
    )
