from flask import Flask, request, jsonify, render_template
from filef import find_items, convert_to_dict

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search-item', methods=['GET'])
def search_item():
    target_substring = request.args.get('substring', '')
    root_dir = r"C:\Users\yan.silva\OneDrive - Adventistas"
    
    data = find_items(root_dir, target_substring)
    data = convert_to_dict(data)
    
    # Return JSON response using jsonify
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
