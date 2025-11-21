from flask import Flask, request, jsonify  # ← добавили импорты

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Serverless! 🚀\n", 200, {'Content-Type': 'text/plain'}

# НОВЫЙ ЭНДПОИНТ
@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()  # Получаем JSON из запроса
    return jsonify({
        "status": "received",
        "you_sent": data,
        "length": len(str(data)) if data else 0
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)