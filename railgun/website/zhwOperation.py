from zinsertHw import session, User, HwType
import random


class HwOperation(object):

    def __init__(self, hwtype):
        self.hwtype = hwtype
        useriter = session.query(User).all()
        self.users = [user for user in useriter]
        the_type = session.query(HwType).filter_by(type=hwtype).first()
        self.hws = the_type.hws

    def release(self):
        for user in self.users:
            user.hws.append(random.choice(self.hws))
            session.add(user)
            session.flush()

    def delete(self):
        for user in self.users:
            for hw in user.hws:
                if hw.hw_type.type == self.hwtype:
                    user.hws.pop(user.hws.index(hw))
            session.add(user)
            session.flush()

if __name__ == '__main__':
    hwOp = HwOperation('API')
    print hwOp.name
