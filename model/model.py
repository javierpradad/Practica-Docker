from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/app', methods=['POST'])
def sum_numbers():
    data = request.get_json()
    num1 = data.get('num1', 0)
    num2 = data.get('num2', 0)
    result = num1 + num2
    return jsonify({'sum': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)