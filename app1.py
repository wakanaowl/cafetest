from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello, World!!!"

#追加
@app.route('/json',methods=['POST'])
def json():
    #受け取ったjsonをそのまま返す
    json = request.json
    return json

if __name__ == '__main__':
    #app.run(host='0.0.0.0',port=5000)
    app.run(host='0.0.0.0')
    #app.run()