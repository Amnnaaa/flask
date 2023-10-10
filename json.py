from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/json-example', methods=['GET'])
def json_example():
    data = {
        'name': 'John Doe',
        'age': 30,
        'city': 'Example City'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
