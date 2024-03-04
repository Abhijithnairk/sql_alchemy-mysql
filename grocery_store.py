from sqlalchemy import ForeignKey, Float, func
from sqlalchemy.orm import relationship
from urllib.parse import quote_plus
from sqlalchemy import create_engine, Column, String, Integer, MetaData, Table
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class NormalizedPrices(Base):
    _tablename_ = 'r_normalized_prices'
    grocery_id = Column(Integer, ForeignKey('reliance.ID'), primary_key=True)  # Add ForeignKey here
    price = Column(Float)
    uom = Column(String(50))

class RelianceGroceries(Base):
    _tablename_ = 'reliance'
    ID = Column(Integer, primary_key=True)
    NAME = Column(String(10), nullable=False)
    PRICE = Column(Integer)
    CATEGORIES = Column(String(10))

    # Define the foreign key relationship
    normalized_prices = relationship('NormalizedPrices', backref='groceries', foreign_keys=[NormalizedPrices.grocery_id])

class WNormalizedPrices(Base):
    _tablename_ = 'wnormalized_prices'
    grocery_id = Column(Integer, ForeignKey('wegmans_groceries.ID'), primary_key=True)  # Add ForeignKey here
    price = Column(Float)
    uom = Column(String(50))
    
class WegmansGroceries(Base):
    _tablename_ = 'wegmans_groceries'
    ID = Column(Integer, primary_key=True)
    NAME = Column(String(10), nullable=False)
    PRICE = Column(Integer)
    CATEGORIES = Column(String(10))

    # Define the foreign key relationship
    normalized_prices = relationship('WNormalizedPrices', backref='groceries', foreign_keys=[WNormalizedPrices.grocery_id])



username = 'rotech_usr'
password = 'Rotech@123'
database_name = 'grocery'
encoded_password = quote_plus(password)

engine = create_engine(f"mysql+pymysql://{username}:{encoded_password}@localhost/{database_name}")

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()