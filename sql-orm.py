from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql:///chinook")
base = declarative_base()

# create class based model for artist table
class Artist(base):
    """something"""
    __tablename__ = "artist"
    artist_id = Column(Integer, primary_key=True)
    name = Column(String)

# for album table
class Album(base):
    """something"""
    __tablename__ = "album"
    album_id = Column(Integer, primary_key=True)
    title = Column(String)
    artist_id = Column(Integer, ForeignKey("Artist.artist_id"))

# for track table
class Track(base):
    """something"""
    __tablename__ = "track"
    track_id = Column(Integer, primary_key=True)
    name = Column(String)
    album_id = Column(Integer, ForeignKey("Album.album_id"))
    media_type_id = Column(Integer, primary_key=False)
    genre_id = Column(Integer, primary_key=False)
    composer = Column(String)

# instead of connection to db direct, req a session
# create new instance of sessionmaker, then point to engine (db)
Session = sessionmaker(db)
# opens actual session by calling the session subclass
session = Session()

#create db using declarative base subclass
base.metadata.create_all(db)

# query 1 - select all records from "artist" table
# artists = session.query(Artist)
# for artist in artists:
#    print(artist.artist_id, artist.name, sep=" | ")

# Q 2
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.name)


# query 3 - only queen from artist table
# artist = session.query(Artist).filter_by(name="Queen").first()
# print(artist.artist_id, artist.name, sep=" | ")


# query 4 - only queen from artist table
# artist = session.query(Artist).filter_by(artist_id=51).first()
# print(artist.artist_id, artist.name, sep=" | ")


# query 5 - albums with id 51 from album table
# albums = session.query(Album).filter_by(artist_id=51)
# for album in albums:
#     print(album.album_id, album.title, sep=" | ")

# query 6 - only queen tracks from track table
tracks = session.query(Track).filter_by(composer="Queen")
for track in tracks:
    print(track.track_id, track.name, track.composer, sep=" | ")
    