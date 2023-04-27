import sqlalchemy
from sqlalchemy import Column, Integer, ForeignKey

from .db_session import SqlAlchemyBase


class Ticket(SqlAlchemyBase):
    __tablename__ = 'tickets'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    start = Column(
        Integer,
        ForeignKey('cosmodrome.id', ondelete='CASCADE'),
        nullable=False,
    )
    finish = Column(
        Integer,
        ForeignKey('cosmodrome.id', ondelete='CASCADE'),
        nullable=False,
    )
    date = sqlalchemy.Column(sqlalchemy.String)
    price = sqlalchemy.Column(sqlalchemy.Integer)
