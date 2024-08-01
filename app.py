from flask import Flask, request, jsonify, render_template
import subprocess

import filef

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-script')
def run_script():
    result = subprocess.run(['python', 'test.py'], capture_output=True, text=True)
    return jsonify(output=result.stdout, error=result.stderr)

@app.route('/search-item', methods=['GET'])
def search_item():
    target_substring = request.args.get('substring', '')
    root_dir = r"C:\Users\yan.silva\OneDrive - Adventistas"
    
    results = filef.find_items(root_dir, target_substring)
    
    return jsonify(results)

if  __name__ == '__main__':
    app.run(debug=True)