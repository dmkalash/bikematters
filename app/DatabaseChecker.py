from orm import orm
class DatabaseChecker(Base):
    def add(self, id=None, login=None,email=None,name=None,birthday=None,passhash=None,occupation=None,about=None,gender=None):
        u = User(id, login, email,name,birthday,passhash,occupation,about,gender)
        db_session.add(u)
        db_session.commit()

