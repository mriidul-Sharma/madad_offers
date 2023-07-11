from flask import Flask
from flask import request
from routes.endpoints import *
from models.models import *
from flask_pymongo import PyMongo


app = Flask(__name__)

# app.register_blueprint(trial_app)

@app.route("/generate_offer", methods = ["POST"])
def generate_offer():
    # The functionality is going to collect the data with respect to the offers inserted and save it into the database.
    try:
        # requesting the data from the body after hitting the request,
        data = request.get_json()

        # inserting the data into the DB with collection named as Offers
        db.offers.insert_one({"coupon_code" : data["coupon_code"], 
                            "discount_value" : data["discount_value"],
                            "discount_type" : data["discount_type"],
                            "valid_from" : data["valid_from"],
                            "valid_to" : data["valid_to"],
                            "number_of_time" : data["number_of_time"],
                            "description" : data["description"]
                            })
        response = {
            "success": True,
            "messsage": "The data got inserted into the DB successfully."
        }, 200

    except Exception as e:
        response = {
            "success": False,
            "message": str(e)
        }, 400
    
    return response

@app.route("/get_all_offers", methods = ["GET"])
def get_all_offers():
    # This will return all the offers, will be accessed by the ADMIN
    try:
        all_coupons = []
        data = db.offers.find()
        for each in data:
            all_coupons.append(each['coupon_code'])

        response = {
            "all_coupons" : all_coupons,
            "success" : True
        }, 200

        return response


    except Exception as e:
        response = {
            "success": False,
            "message": str(e)
        }, 400

    return response

@app.route("/delete_offer", methods = ["DELETE"])
def delete_offer():
    #This is gonna delete the specific coupon code object from the DB
    try:

        offer_to_delete = request.args.get("coupon_code")
        todo = db.offers.delete_one({'coupon_code': offer_to_delete})

        return {
            "Success" : True,
            "message" : "Deletion was Successful"
        }

    except Exception as e:
        response = {
            "success": False,
            "message": str(e)
        }, 400

    return response





if __name__ == '__main__':  
    app.run()