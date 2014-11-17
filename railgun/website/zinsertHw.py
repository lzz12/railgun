from sqlalchemy import create_engine, schema, Table
from sqlalchemy.orm import create_session, mapper, relation
from . import webconfig

db = create_engine(webconfig.SQLALCHEMY_DATABASE_URI)
metadata = schema.MetaData(db)
session = create_session()

users = Table('users', metadata, autoload=True)
finalscore = Table('finalscore', metadata, autoload=True)
handins = Table('handins', metadata, autoload=True)
hwtypes = Table('hwtypes', metadata, autoload=True)
hws = Table('hws', metadata, autoload=True)
userHw = Table('userHw', metadata, autoload=True)


class User(object):
    pass


class FinalScore(object):
    pass


class Handin(object):
    pass


class HwType(object):

    def __init__(self, type=None, is_hidden=True):
        self.type = type
        self.is_hidden = is_hidden

    def __repr__(self):
        return "<HwType:%s is %s>" % (self.type, self.is_hidden)


class Hw(object):

    def __init__(self, uuid=None, type_id=None):
        self.uuid = uuid
        self.type_id = type_id

    def __repr__(self):
        return "<homework:%s>" % (self.uuid)

mapper(User, users)
mapper(HwType, hwtypes)
mapper(Hw, hws, properties={
    'hw_type': relation(HwType, backref='hws'),
    'users': relation(User, secondary=userHw, backref='hws')
})

# onehw = Hw()
# oneType = HwType()
# onehw.uuid = '9f286333b778488c9a14d66aaf559f48'
# onehw.is_hidden = True
# onehw.hw_type = oneType
# oneType.type = 'Arithmetic API'
# oneType.baseTime = DateTime(2015, 9, 12, 23, 59, 59)

# oneType.hws.append(onehw)
# session.add(oneType)
# session.flush()

# onehw = Hw()
# oneType = HwType()
# onehw.uuid = 'ad19289bde3b496b88ef2421b2f2e153'
# onehw.is_hidden = True
# onehw.hw_type = oneType
# oneType.type = 'Blackbox Test'
# oneType.hws.append(onehw)
# session.add(oneType)
# session.flush()

# onehw = Hw()
# oneType = HwType()
# onehw.uuid = 'b388ad5b25ee44bbac9be46c43851768'
# onehw.is_hidden = True
# onehw.hw_type = oneType
# oneType.type = 'Format Path'
# oneType.hws.append(onehw)
# session.add(oneType)
# session.flush()

# onehw = Hw()
# oneType = HwType()
# onehw.uuid = '69e937823ac04e0fbe8cfefd0bb197ab'
# onehw.is_hidden = True
# onehw.hw_type = oneType
# oneType.type = 'Whitebox Test'
# oneType.hws.append(onehw)
# session.add(oneType)
# session.flush()

# onehw = Hw()
# oneType = HwType()
# onehw.uuid = 'bfff167aaf2a471a9bc4d2cb56c15ede'
# onehw.is_hidden = True
# onehw.hw_type = oneType
# oneType.type = 'Learn xUnit'
# oneType.hws.append(onehw)
# session.add(oneType)
# session.flush()
