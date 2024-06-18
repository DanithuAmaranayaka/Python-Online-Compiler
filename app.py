from flask import Flask, request, jsonify, send_from_directory
import subprocess
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def serve_frontend():
    return send_from_directory('frontend', 'index.html')

@app.route('/run', methods=['POST'])
def run_code():
    code = request.json.get('code')
    try:
        # Write code to a temporary file
        with open('temp.py', 'w') as f:
            f.write(code)
        # Run the code using subprocess
        result = subprocess.run(['python3', 'temp.py'], capture_output=True, text=True, timeout=5)
        return jsonify({'output': result.stdout, 'errors': result.stderr})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
