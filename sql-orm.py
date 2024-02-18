from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql:///chinook")
base = declarative_base()

# create class based model for artist table
class artist(base):
    __tablename__ = "artist"
    artist_id = Column(Integer, primary_key=True)
    name = Column(String)

# for album table
class album(base):
    __tablename__ = "album"
    album_id = Column(Integer, primary_key=True)
    title = Column(String)
    artistId = Column(Integer, ForeignKey("artist.artist_id"))

# for track table
class track(base):
    __tablename__ = "track"
    track_id = Column(Integer, primary_key=True)
    name = Column(String)
    album_id = Column(Integer, ForeignKey("album.album_id"))
    media_type_id = Column(Integer, primary_key=False)
    genre_id = Column(Integer, primary_key=False)
    composer = Column(String)
    milliseconds = Column(Integer, primary_key=False)
    bytes = Column(Integer, primary_key=False)
    unit_price = Column(Float)

# instead of connection to db direct, req a session
# create new instance of sessionmaker, then point to engine (db)
Session = sessionmaker(db)
# opens actual session by calling the session subclass
session = Session()

#create db using declarative base subclass
base.metadata.create_all(db)


# query 1 - select all records from "artist" table
artists = session.query(Artist)
for artist in artists:
    print(artist.artist_id, artist.name, sep=" | ")

# Q 2

# query 3 - only queen from artist table


# query 4 - only queen from artist table


# query 5 - albums with id 51 from album table 


# query 6 - only queen tracks from track table