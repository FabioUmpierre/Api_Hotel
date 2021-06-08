from sql_alchemy import DB

class HotelModel(DB.Model):
    __tablename__ = 'hoteis'

    id = DB.Column(DB.String, primary_key=True)
    name = DB.Column(DB.String(80))
    stars = DB.Column(DB.Float(precision=1))
    dayli = DB.Column(DB.Float(precision=2))
    city = DB.Column(DB.String(40))
   
    def __init__(self,id, name, stars, dayli, city):
        self.id = id
        self.name = name
        self.stars = stars
        self.dayli = dayli
        self.city = city

    def json(self):
        return{
            'id' : self.id,
            'name' : self.name,
            'stars' : self.stars,
            'dayli' : self.dayli,
            'city' : self.city
        }    

    @classmethod
    def find_hotel(cls, id):
        hotel = cls.query.filter_by(id=id).first()
        if hotel:
            return hotel
        return None

    def save_hotel(self):
        DB.session.add(self)
        DB.session.commit()

    def update_hotel(self, name, stars, dayli, city):
        self.name = name
        self.stars = stars
        self.dayli = dayli
        self.city = city

    def delete_hotel(self):
        DB.session.delete(self)
        DB.session.commit()    