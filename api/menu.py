from flask_restful import Resource, Api, reqparse
from dbconn import Database


class Menu:
    def __init__(self):
        self.database = Database()
        self.database.create_menu_table()

    def create_menu(self):
        parser = reqparse.RequestParser()
        parser.add_argument('menu_name',
                            type=str,
                            required=True,
                            help='Field cannot be blank')

        parser.add_argument('price',
                            type=int,
                            required=True,
                            help='Field cannot be blank')

        data = parser.parse_args()

        if self.find_menu_by_name(data['menu_name']):
            return {'message': 'Item already exists'}, 409

        query = ("INSERT INTO menu(menu_name, price)\
            VALUES('{}', {})\
            RETURNING menu_id, menu_name, price")

        self.database.cursor.execute(query.format(data['menu_name'],
            data['price']))

        return {'message': 'Item successfully added'}, 200

    # def get_all_items(self):
    #     query = "SELECT * FROM menu"
    #     self.database.cursor.execute(query)
    #     row = self.database.cursor.fetchall()
    #     results = []
    #     if row:
    #         for item in row:
    #             results.append({
    #                 'foodId':item[0],
    #                 'name':item[1],
    #                 'description':item[2],
    #                 'price':item[3]
    #                 })
    #         return jsonify(results)
    #     else:
    #         item = None
    #         return {'message': 'Menu is unavailable'}

    def find_menu_by_name(self, menu_name):
        query = "SELECT * FROM  menu WHERE menu_name = '{}'"
        self.database.cursor.execute(query.format(menu_name))
        row = self.database.cursor.fetchone()
        return row


