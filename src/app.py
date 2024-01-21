from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    { "done": True, "label": "Sample Todo 1" },
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    todos.append(request.json)    
    json_text = jsonify(todos) 
    # print("Incoming request with the following body", todos)
    return json_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    json_text = jsonify(todos)
    print("This is the position to delete:", position)
    return json_text

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)