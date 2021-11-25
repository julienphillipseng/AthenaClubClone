from flask import Flask
from flask_restful import Resource, Api
import json


app = Flask(__name__)
api = Api(app)

products = json.loads(json.dumps({"products": [
    {"name": "The Razor Kit", "price": 9, "imageUrl": "https://athena-club.s3.amazonaws.com/2021/09/Coral_RazorKit-Recovered-1.png",
     "description": "Your new favourite razor, available in 6 colors. Yes, even black and white.", "rating": 92},
    {"name": "Cloud Shave Foam", "price": 9, "imageUrl": "https://athena-club.s3.amazonaws.com/2021/04/WFLjPGxt-Shave_Foam.png",
     "description": "Looks like whipped cream, smells like roses. Leaves skin smooth and soothed.", "rating": 92},
    {"name": "Creamy Body Wash", "price": 15, "imageUrl": "https://athena-club.s3.amazonaws.com/2021/09/ocoPuaOI-KS5LDmid-Pink_BodyWash.png",
     "description": "Rich, creamy + packed with skin-loving nutrients. Bonus: you can shave with it.", "rating": 100},
    {"name": "Soft Face Wipes", "price": 10, "imageUrl": "https://athena-club.s3.amazonaws.com/2021/06/WhVMypfF-Soft_Face_Wipes-v2-2.png",
     "description": "Our super soft wipes leave your face clean, nourished, and makeup-free.", "rating": 90},
    {"name": "Dewy Body Lotion", "price": 15, "imageUrl": "https://athena-club.s3.amazonaws.com/2021/09/xtNCZqtt-Navy_BodyLotion-1.png",
     "description": "With vitamins and antioxidants, our lotion leaves skin dewy and healthy.", "rating": 100},
    {"name": "All Day Deo", "price": 12, "imageUrl": "https://athena-club.s3.amazonaws.com/2021/04/mCzXDz4t-Deo-No.1.png",
     "description": "Our plant-based deo keeps you fresh all day, every day. Available in 3 scents.", "rating": 92}
]}))


class Products(Resource):
    def get(self):
        return products, 200, {'Access-Control-Allow-Origin': '*'}


api.add_resource(Products, "/products")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
