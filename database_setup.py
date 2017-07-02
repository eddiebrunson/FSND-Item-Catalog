from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Genre(Base):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class Movie(Base):
    __tablename__ = 'movie'

    name = Column(String(80), nullable=False)
    cover_url = Column(String(250))
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    MPAA_film_rating = Column(String(8))
    IMDb_rating = Column(String(8))
    youtube_url = Column(String(250))
    gross = Column(String(8))
    release_date = Column(String(8))
    runtime = Column(String(8))
    genre_id = Column(Integer, ForeignKey('genre.id'))
    genre = relationship(Genre)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'cover_url': self.cover_url,
            'description': self.description,
            'gross': self.gross,
            'MPAA_film_rating': self.MPAA_film_rating,
            'release_date': self.release_date,
            #'genre': self.genre,
            'id': self.id,
            'runtime': self.runtime,
            'IMDb_rating': self.IMDb_rating,
            'youtube_url': self.youtube_url
        }


engine = create_engine('sqlite:///samplemovies.db')


Base.metadata.create_all(engine)