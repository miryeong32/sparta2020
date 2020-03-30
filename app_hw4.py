from flask import Flask, render_template, jsonify, request

app_hw4 = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework

@app_hw4.route('/')
def home()
    return render_template('homework4.html')

@app_hw4.rout('/orders', methods=['POST'])
def write_order():
    name_receive = request.form['name_give']
    number_receive = request.form['number_give']
    address_receive = request.form['address_give']
    tel_receive = request.form['tel_give']

    order = {
        'name': name_receive,
        'number': number_receive,
        'address': address_receive,
        'tel': tel_receive
    }

    db.orders.insert_one(order)
    return jsonify({'result':'success', 'msg': '주문이 완료되었습니다.'})


@app_hw4.route('/orders', method=['GET'])
def read_orders():
    orders = list(db.orders.find({},{'_id':0}))
    return jsonify({'result':'success','orders':orders})

if __name__ == '__main__':
    app_hw4.run('127.0.0.1',port=5000,debug=True)