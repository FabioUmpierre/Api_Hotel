from flask_restful import Resource, reqparse
from models.hotel import HotelModel

class Hoteis(Resource):
    def get(self):
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]} # SELECT * FROM hoteis

class Hotel(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('name', type=str, required=True, help="The field 'name' cannot be left blank.")
    atributos.add_argument('stars')
    atributos.add_argument('dayli')
    atributos.add_argument('city')

    def get(self, id):
        hotel = HotelModel.find_hotel(id)
        if hotel:
            return hotel.json()
        return {'message': 'Hotel not found.'}, 404

    def post(self, id):
        if HotelModel.find_hotel(id):
            return {"message": "Hotel id '{}' already exists.".format(id)}, 400 #Bad Request

        dados = Hotel.atributos.parse_args()
        hotel = HotelModel(id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {"message": "An error ocurred trying to create hotel."}, 500 #Internal Server Error
        return hotel.json(), 201

    def put(self, id):
        dados = Hotel.atributos.parse_args()
        hotel = HotelModel(id, **dados)

        hotel_encontrado = HotelModel.find_hotel(id)
        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados)
            hotel_encontrado.save_hotel()
            return hotel_encontrado.json(), 200
        hotel.save_hotel()
        return hotel.json(), 201

    def delete(self, id):
        hotel = HotelModel.find_hotel(id)
        if hotel:
            hotel.delete_hotel()
            return {'message': 'Hotel deleted.'}
        return {'message': 'Hotel not found.'}, 404

