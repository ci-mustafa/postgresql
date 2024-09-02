from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Artist" table
class Artist(base):
    __tablename__ = "Artist"
    artist_id = Column(Integer, primary_key=True)
    name = Column(String)


# create a class-based model for the "Album" table
class Album(base):
    __tablename__ = "Album"
    Aalbum_id = Column(Integer, primary_key=True)
    title = Column(String)
    artist_id = Column(Integer, ForeignKey("Artist.artist_id"))


# create a class-based model for the "Track" table
class Track(base):
    __tablename__ = "Track"
    track_id = Column(Integer, primary_key=True)
    name = Column(String)
    album_id = Column(Integer, ForeignKey("Album.album_id"))
    mediaTypeId = Column(Integer, primary_key=False)
    genreId = Column(Integer, primary_key=False)
    composer = Column(String)
    milliseconds = Column(Integer, primary_key=False)
    bytes = Column(Integer, primary_key=False)
    unitPrice = Column(Float)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# Query 1 - select all records from the "Artist" table
artists = session.query(Artist)
for artist in artists:
    print(artist.artist_id, artist.name, sep=" | ")

# Query 2 - select only the "Name" column from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)

# Query 3 - select only "Queen" from the "Artist" table
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# Query 6 - select all tracks where the composer is "Queen" from the "Track" table
# tracks = session.query(Track).filter_by(Composer="Queen")
# for track in tracks:
#     print(
#         track.TrackId,
#         track.Name,
#         track.AlbumId,
#         track.MediaTypeId,
#         track.GenreId,
#         track.Composer,
#         track.Milliseconds,
#         track.Bytes,
#         track.UnitPrice,
#         sep=" | "
#     )