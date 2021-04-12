from sqlalchemy import MetaData, Table, Integer, String, Column, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

SQLITE = 'sqlite'
MYSQL = 'mysql'

Base = declarative_base()

class platoons(Base):
    __tablename__ = 'platoon'

    name = Column(String(20), primary_key=True)
    size = Column(Integer)
    captain = relationship('solider', backref='platoon')


class solider(Base):
    __tablename__ = 'solider'

    name = Column(String(20), primary_key=True)
    age = Column(Integer)
    rank = Column(String(20))
    own_gun = relationship('gun', backref='solider')

class gun(Base):
    __tablename__ = 'gun'

    name = Column(String(20), primary_key=True)
    ammo = Column(Integer)
    ammo_type = Column(String(20))

class Start:
    DB_ENGINE = {
        SQLITE: 'sqlite:///{DB}',
        MYSQL: 'mysql+mysqlconnector://{USERNAME}:{PASSWORD}@localhost/{DB}'
    }

    def __init__(self, dbtype='sqlite', username='', password='', dbname='persons'):
        dbtype = dbtype.lower()

        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname, USERNAME=username, PASSWORD=password)
            self.engine = create_engine(engine_url, echo=True)
        else:
            print('Error! DBtype not found')

        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

db = Start()