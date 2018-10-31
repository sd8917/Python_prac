from flask import Flask, jsonify, request

app = Flask(__name__)

languages = [{'name': 'javascript'}, {'name': 'Python'}, {'name': 'perl'}, {'name': 'Swift'}, {'name': 'java'}, {'name': 'Mysql'}]


@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': 'It works !!'})


@app.route('/lang', methods=['GET'])
def returnAll():
    return jsonify({'languages':languages})


@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
    langs = [language for language in languages if language['name'] == name]
    return jsonify({'language': langs[0]})


@app.route('/lang/<string:name>', methods=['PUT'])
def editOne(name):

    langs = [language for language in languages if language['name'] == name]
    langs[0]['name'] = request.json['name']
    return jsonify({'languages': langs[0]})


if __name__ == '__main__':
    app.run(debug=True, port=8080)
