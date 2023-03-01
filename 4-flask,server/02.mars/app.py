from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://siwon:rlaznf11@cluster0.icysouv.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsiwon

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/mars", methods=["POST"])
def mars_post():
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']

    order_info = {
        'name': name_receive,
        'address': address_receive,
        "size": size_receive
    }

    db.orders.insert_one(order_info)
    return jsonify({'msg':'Order successfully saved'})

@app.route("/mars", methods=["GET"])
def mars_get():
    return jsonify({'msg':'GET completed!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)