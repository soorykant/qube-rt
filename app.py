from flask import Flask, request, render_template, redirect, url_for
import json

app = Flask(__name__)
app.debug = True

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/spaceship/optimize", methods=["POST"])
def spaceship():
    data = json.loads(request.form['payload'])

    contracts = data['data']
    contracts.sort(key=lambda x: x["start"] + x["duration"])
    curr_time = 0
    curr_profit = 0
    path = []
    for contract in contracts:
        if contract["start"] >= curr_time:
            curr_time = contract["start"] + contract["duration"]
            curr_profit += contract["price"]
            path.append(contract["name"])
        
    response = {"income": curr_profit, "path": path}
    return render_template('response.html', response=response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
