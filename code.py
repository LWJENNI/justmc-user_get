from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

@app.route('/decode', methods=['POST'])
def decode_base64():
    request_data = request.get_json()

    if 'base64' not in request_data:
        return jsonify({'error': 'Missing base64 key in JSON'}), 400

    base64_data = request_data['base64']
    
    try:
        decoded_text = base64.b64decode(base64_data).decode('utf-8')
        return jsonify({'decoded_text': decoded_text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
