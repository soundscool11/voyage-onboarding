from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://siwon:rlaznf11@cluster0.icysouv.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsiwon

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']
    doc = { 
        'bucket': bucket_receive,
        'completed': 0
    }
    db.buckets.insert_one(doc)
    return jsonify({'msg': 'Your wish is saved!'})

@app.route("/bucket-update", methods=["POST"])
def bucket_completed():
    not_completed = { 'completed': 0 }
    completed = {"$set": {'completed': 1 }}
    db.buckets.update_one(not_completed, completed)
    return jsonify({'msg': 'Your wish is completed!'})
    
@app.route("/bucket", methods=["GET"])
def bucket_get():
    all_buckets = list(db.buckets.find({}, {'_id': False}))
    return jsonify({'msg': all_buckets})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)