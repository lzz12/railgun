from sqlalchemy import create_engine, schema, Table
from sqlalchemy.orm import create_session, mapper, relation
# from . import webconfig
from config import HOMEWORK_DIR, RAILGUN_ROOT
import os
from datetime import datetime

SQLALCHEMY_DATABASE_URI = (
    'sqlite:///%s' % os.path.join(RAILGUN_ROOT, 'db/main.db')
)
db = create_engine(SQLALCHEMY_DATABASE_URI)

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

from datetime import datetime

class Homework():
    def __init__(self):
        self.uuid=None
        self.name=None

class InsertHws(object):
    def __init__(self,hwdir):
        self.hwdir=hwdir
        self.files=[]
        self.items=[]
        # self.items.uuids=[]
        # self.items.names=[]
        for fn in os.listdir(hwdir):
            fp = os.path.join(hwdir,fn)
            file=os.path.join(fp,'hw.xml')
            if (os.path.isdir(fp) and
                os.path.isfile(file)):
                self.files.append(file)
        self.load()

    def load(self):
        import re
        str1=r"<uuid>\s*(.*)\s*</uuid>"
        str2=r'''<name\s*lang\s*=\s*"en">\s*(.*)\s*</name>'''
        for file in self.files:
            log = open(file,'r')
            text=log.read()
            m1=re.search(str1,text)
            m2=re.search(str2,text)
            item=Homework()
            item.uuid=m1.group(1)
            item.name=m2.group(1)
            self.items.append(item)
            log.close()
    def insertHw(self,basetime=datetime(2015, 9, 12, 23, 59, 59)):
        typelistx=session.query(HwType).all()
        typelist=[itemx for itemx in typelistx]
        for item in self.items:
            try:
                #namelist=[hwtypex.type for hwtypex in typelist]
                flag=False
                onehw = Hw()
                onehw.uuid = item.uuid
                for typeitem in typelist:
                    if item.name == typeitem.type:
                        onehw.hw_type=typeitem
                        flag=True
                if not flag:
                    oneType=HwType()
                    onehw.hw_type = oneType
                    oneType.type = item.name
                    oneType.is_hidden=True
                    oneType.basetime = basetime
                    oneType.hws.append(onehw)
                    typelist.append(oneType)
                session.add(onehw)
                session.flush()

            except:
                #print "can't insert"
                pass



hw = InsertHws(HOMEWORK_DIR)
hw.insertHw()
