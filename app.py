from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Load dataset
with open('data.json') as f:
    routes = json.load(f)

@app.route('/route', methods=['GET'])
def get_route():
    source = request.args.get('source')
    destination = request.args.get('destination')
    preference = request.args.get('preference')

    options = [r for r in routes if r["from"].lower() == source.lower() 
               and r["to"].lower() == destination.lower()]

    if not options:
        return jsonify({"message": "No route found"})

    if preference == "time":
        best = min(options, key=lambda x: x["time"])
    elif preference == "cost":
        best = min(options, key=lambda x: x["cost"])
    else:
        best = max(options, key=lambda x: x["safety"])

    return jsonify(best)

if __name__ == '__main__':
    app.run(debug=True)
