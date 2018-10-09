from flask import Flask, request, abort, jsonify
from flask_restful import Resource, Api, reqparse
from api.menu import Menu

app = Flask(__name__)

api = Api(app)

menu = Menu()

class Welcome(Resource):
    def get(self):
        return 'welcome to my sunny days'

class Menu(Resource):
    def post(self):
        return menu.create_menu()



    # def create_item(self):
    #     parser = reqparse.RequestParser()
    #     parser.add_argument('menu_name',
    #                         type=str,
    #                         required=True,
    #                         help='Field cannot be blank')
        
    #     parser.add_argument('price',
    #                         type=int,
    #                         required=True,
    #                         help='Field cannot be blank')

    #     data = parser.parse_args()

    #     if self.find_menu_by_name(data['name']):
    #         return {'message': 'Item already exists'}, 409

    #     query = ("INSERT INTO menu(menu_name, price)\
    #         VALUES('{}', {})\
    #         RETURNING menu_id, menu_name, price")

    #     self.database.cursor.execute(query.format(data['menu_name'],
    #        data['price']))

    #     return {'message': 'Item successfully added'}, 200

    # # def get_all_items(self):
    # #     query = "SELECT * FROM menu"
    # #     self.database.cursor.execute(query)
    # #     row = self.database.cursor.fetchall()
    # #     results = []
    # #     if row:
    # #         for item in row:
    # #             results.append({
    # #                 'foodId':item[0],
    # #                 'name':item[1],
    # #                 'description':item[2],
    # #                 'price':item[3]
    # #                 })
    # #         return jsonify(results)
    # #     else:
    # #         item = None
    # #         return {'message': 'Menu is unavailable'}

    # def find_menu_by_name(self, name):
    #     query = "SELECT * FROM  menu WHERE menu_name = '{}'"
    #     self.database.cursor.execute(query.format(name))
    #     row = self.database.cursor.fetchone()
    #     return row

    # def find_menu_by_description(self, description):
    #     query = "SELECT * FROM  menu WHERE description = '{}'"
    #     self.database.cursor.execute(query.format(description))
    #     row = self.database.cursor.fetchone()
    #     return row
api.add_resource(Welcome, '/')
api.add_resource(Menu, '/api/v1/menu')
