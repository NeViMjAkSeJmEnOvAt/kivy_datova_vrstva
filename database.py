from sqlalchemy import Integer, String, Column, create_engine
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

    def read_all_solider(self, order = solider.name):
        try:
            result = self.session.query(solider).all()
            return result
        except:
            return False

    def read_all_platoon(self, order = platoons.name):
        try:
            result = self.session.query(platoons).all()
            return result
        except:
            return False

    def read_all_guns(self, order = gun.name):
        try:
            result = self.session.query(gun).all()
            return result
        except:
            return False

    def read_by_solider_age(self, age):
        try:
            result = self.session.query(solider).get(age)
            return result
        except:
            return False

    def read_by_solider_name(self, name):
        try:
            result = self.session.query(solider).get(name)
            return result
        except:
            return False

    def read_by_solider_rank(self, rank):
        try:
            result = self.session.query(solider).get(rank)
            return result
        except:
            return False

    def read_solider_gun(self, age):
        try:
            result = self.session.query(solider).get(gun)
            return result
        except:
            return False

    def read_by_platoon_size(self, size):
        try:
            result = self.session.query(platoons).get(size)
            return result
        except:
            return False

    def read_by_gun_ammo(self, ammo):
        try:
            result = self.session.query(gun).get(ammo)
            return result
        except:
            return False

    def read_by_gun_ammo_type(self, ammo_type):
        try:
            result = self.session.query(gun).get(ammo_type)
            return result
        except:
            return False

    def create_solider(self, solider):
        try:
            self.session.add(solider)
            self.session.commit()
            return True
        except:
            return False

    def create_platoon(self, platoon):
        try:
            self.session.add(platoon)
            self.session.commit()
            return True
        except:
            return False

    def create_gun(self, gun):
        try:
            self.session.add(gun)
            self.session.commit()
            return True
        except:
            return False

    def update(self):
        try:
            self.session.commit()
            return True
        except:
            return False

    def delete(self, name):
        try:
            solider = self.read_by_solider_name(name)
            self.session.delete(solider)
            self.session.commit()
            return True
        except:
            return False


db = Start(dbtype='sqlite', dbname='persons.db')

db.create_solider(solider)


