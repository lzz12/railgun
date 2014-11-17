import random


def urandom():
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    digits = '1234567890'
    codes = letters + digits
    uuid = ''
    for i in xrange(32):
        uuid += random.choice(codes)
    return uuid


class XmlManager(object):

    def __init__(self, filedir, **args):
        self.filedir = filedir
        self.uuid = urandom()
        self.names = args['names']
        self.deadlines = args['deadlines']

    def generateXml(self):
        try:
            xml = open(self.filedir, 'w')
            print >> xml, '''<?xml version="1.0"?>'''
            print >> xml, '<homework>'
            print >> xml, '  ', "<uuid>%s</uuid>" % self.uuid
            print >> xml, '  ', '''<names>
        <name lang="zh-cn">%s</name>
        <name lang="en">%s</name>
        </names>''' % self.names
            print >> xml, '  ', '<deadlines>'

            for i in xrange(4):
                print >>xml, '  ', '''<due>
        <timezone>%(timezone)s</timezone>
        <date>%(date)s</date>
        <scale>%(scale)s</scale>
    </due>''' % self.deadlines[i]

            print >> xml, ' ', '</deadlines>'
            print >> xml, ' ', '<files/>'
            print >> xml, '</homework>'
        except:
            return 'fail in create xml'

if __name__ == '__main__':

    manager = XmlManager('1.txt', names=('API', 'Arithmetic API'),
                         deadlines={'timezone': 'Asia/Shanghai',
                                    'date': '2015-9-12 23:59:59',
                                    'scale': '1.0'})
    manager.generateXml()
