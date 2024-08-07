from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/test', methods=['GET', 'POST'])
def test_api():
    if request.method == 'POST':
        data = request.get_json()
        return jsonify({"message": "POST request received!", "data": data}), 200
    else:
        return jsonify({"message": "GET request received!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
