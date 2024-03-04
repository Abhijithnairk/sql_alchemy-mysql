from sqlalchemy import create_engine, Column, String, Integer, CHAR
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.dialects.mysql import pymysql

Base = declarative_base()

class Person(Base):
    _tablename_ = "people"
    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)
    
    def _init_(self, ssn, first, last, gender, age):
        self.ssn = ssn
        self.firstname = first
        self.lastname = last
        self.gender = gender
        self.age = age
            
    def _repr_(self):
        return f"({self.ssn}) {self.firstname} {self.lastname} ({self.gender},{self.age})"

# Corrected engine creation with MySQL details
engine = create_engine('mysql://abhijith_user:Abhi@1212@localhost/GROCERY_STORE')

# Now, you can use this engine to connect to the MySQL database
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# Creating and adding a person using the class
person_instance = Person(121212, "mike", "smith", "male", 35)
session.add(person_instance)
session.commit()

# Creating and adding multiple persons using the class
p1 = Person(1, "john", "jacob", "male", 36)
p2 = Person(2, "dulqer", "salman", "male", 38)
p3 = Person(3, "siddarth", "malhothra", "male", 40)

session.add_all([p1, p2, p3])
session.commit()