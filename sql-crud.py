from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for programmer table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)



# instead of connection to db direct, req a session
# create new instance of sessionmaker, then point to engine (db)
Session = sessionmaker(db)
# opens actual session by calling the session subclass
session = Session()

#create db using declarative base subclass
base.metadata.create_all(db)

# creating records
ada_lovelace = Programmer(
    first_name = "Ada",
    last_name = "Lovelace",
    gender = "female",
    nationality = "British",
    famous_for = "First Programmer"
)

alan_turing = Programmer(
    first_name = "Alan",
    last_name = "Turing",
    gender =  "male",
    nationality = "British",
    famous_for = "Modern Computing"
)

grace_hopper = Programmer(
    first_name = "Grace",
    last_name = "Hopper",
    gender =  "female",
    nationality = "American",
    famous_for = "CBOL language"
)

margaret_hamilton = Programmer(
    first_name = "Margaret",
    last_name = "Hamilton",
    gender =  "female",
    nationality = "American",
    famous_for = "Apollo 11"
)

bill_gates = Programmer(
    first_name = "Bill",
    last_name = "Gates",
    gender =  "male",
    nationality = "American",
    famous_for = "Microsoft"
)

tim_berners_lee = Programmer(
    first_name = "Tim",
    last_name = "Berners-Lee",
    gender =  "male",
    nationality = "British",
    famous_for = "WWW"
)

# add each instance of programmer to session
# session.add(ada_lovelace)
session.add(ada_lovelace)
session.add(grace_hopper)
session.add(margaret_hamilton)
session.add(bill_gates)
session.add(tim_berners_lee)
# commit to database 
session.commit()

# query the database to find all programmers 
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )