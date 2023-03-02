from flask import Flask, render_template, request, jsonify
application = app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://siwon:rlaznf11@cluster0.icysouv.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsiwon

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/fanbook", methods=["POST"])
def fanbook_post():
    nickname_receive = request.form['nickname_give']
    comment_receive = request.form['comment_give']
    
    doc = {
        'nickname': nickname_receive,
        'comment': comment_receive
    }
    db.fanbooks.insert_one(doc)
    return jsonify({'msg': 'Your fan message is saved!'})


@app.route("/fanbook", methods=["GET"])
def fanbook_get():
    all_fanbooks = list(db.fanbooks.find({}, {'_id': False}))
    return jsonify({'msg': all_fanbooks})

if __name__ == '__main__':
   app.run()