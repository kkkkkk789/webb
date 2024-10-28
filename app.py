from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_fivem_players(server_ip, port):
    url = f"http://{server_ip}:{port}/players.json"
    response = requests.get(url)
    if response.status_code == 200:
        players = response.json()
        return players
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    players = None
    error = None
    if request.method == 'POST':
        server_ip = request.form['ip']
        port = request.form['port']
        players = get_fivem_players(server_ip, port)
        if players is None:
            error = "Failed to connect to server or retrieve player data."
    return render_template('index.html', players=players, error=error)

if __name__ == '__main__':
    app.run(debug=True)
