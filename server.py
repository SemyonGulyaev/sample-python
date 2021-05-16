from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello this is the new version!!!"

@app.route("/json")
def getJSON():
    return jsonify({'name':'Semyon',
                    'email':'noc77@gmail.com',
                    'locale':'https://youtube.com'})

@app.route("/routers", methods=['GET'])
def getRouter():
    hostname = request.args.get('hostname')
    return hostname

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, threaded=True)
