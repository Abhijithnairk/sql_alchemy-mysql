from urllib.parse import quote_plus
from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.orm import declarative_base,sessionmaker

Base = declarative_base()

class Employee(Base):
    __tablename__='peoples_tbl'
    id=Column(Integer,primary_key=True)
    name=Column(String(255))
    age=Column(Integer)
    place=Column(String(255))
password = "Abhi@1212"
encode_password = quote_plus(password)
    
engine = create_engine(f"mysql+pymysql://abhijith_user:{encode_password}@localhost/employee",echo=True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

p1 = Employee(name='john',age=30,place='new york')
session.add(p1)
session.commit()



    