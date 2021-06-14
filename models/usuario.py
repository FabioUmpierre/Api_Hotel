from sql_alchemy import DB

class UserModel(DB.Model):
    __tablename__ = 'usuarios'

    user_id = DB.Column(DB.Integer, primary_key=True)
    login = DB.Column(DB.String(40))
    senha = DB.Column(DB.String(40))

    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def json(self):
        return {
            'user_id': self.user_id,
            'login': self.login
            }

    @classmethod
    def find_user(cls, user_id):
        user = cls.query.filter_by(user_id=user_id).first()
        if user:
            return user
        return None

    @classmethod
    def find_by_login(cls, login):
        user = cls.query.filter_by(login=login).first()
        if user:
            return user
        return None

    def save_user(self):
        DB.session.add(self)
        DB.session.commit()

    def delete_user(self):
        DB.session.delete(self)
        DB.session.commit()

