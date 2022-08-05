from flask import Flask, request, jsonify, request
import json
import sqlite3

app = Flask(__name__)


def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("database_file.db")
    except sqlite3.error as e:
        print(e)
    return conn




@app.route("/products", methods=["GET"])
def products():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM new_product_details")
        products = [
            dict(product_name=row[0], price=row[1], quantity=row[2], created_at=row[3], is_active=row[4])
            for row in cursor.fetchall()
        ]
        if products is not None:
            return jsonify(products)



@app.route("/products1", methods=["POST"])
def create_product_item():
    try:
        conn = db_connection()
        cursor = conn.cursor()



        request_data = request.get_json()
        print(request_data)
        if not request_data:
            return jsonify({
                "status" : 422,
                "message" : "request is not appropriate"
            }),422
        product_name = request_data.get('product_name')
        print(request_data.get('product_name'))
        price = request_data.get('price')
        quantity = request_data.get('quantity')
        print(product_name, price, quantity)
        if not product_name:
            return jsonify({
                "status": 422,
                "message": "sorry product_name is required"
            }), 422

        elif not price:
            return jsonify({
                "status": 422,
                "message": "sorry price is required"
            }), 422
        elif not price.isnumeric():
            return jsonify({
                "status": 422,
                "message": "sorry price should not in negative number"
            }), 422

        elif not quantity:
            return jsonify({
                "status": 422,
                "message": "sorry quantity is required"
            }), 422

        # elif price <=0:
        #     return jsonify({
        #         "status": 416,
        #         "message": " The amount can't be negative ,please try again"
        #      }),416

        elif not quantity.isnumeric():
            return jsonify({
               "status": 416,
                "message": "the quantity should not be negative value,kindly try again"
             }), 416
        #
        # elif len(new_product_name) <= 5:
        #     return jsonify({
        #         "status": 422,
        #         "message" : "kindly put a valid name "
        #     }),422
        #
        # elif new_product_name =="" or new_price == "" or new_quantity == "":
        #     return jsonify({
        #         "status": 400,
        #         "message": "sorry you must fill in all the fields"
        #     }),400
        #
        #
        #
        # else:
        #     return jsonify({
        #         "status": 201,
        #         "message": "product_item created successfully" ,
        #         "payload":{
        #             "new_product_name": new_product_name,
        #             "new_price": new_price,
        #             "new_quantity": new_quantity
        #         }
        #
        #     }),201
        #
        #
        # #sql = """ INSERT INTO new_product_details(product_name, price, quantity) VALUES(?,?,?) """
        # #cursor = cursor.execute(sql, (new_product_name, new_price, new_quantity))
        #

    except Exception as e:
        import traceback
        traceback.print_exc()
        print("Error" ,e)
        return jsonify({
            "status":500,
            "message":"something went wrong."
        }),500


if __name__ == "__main__":
    app.run(debug=True)