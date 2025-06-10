from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def home():
    return "Welcome! Visit /client1 or /client2 to chat."

@app.route('/client1')
def client1():
    return render_template('client.html', username="Client 1")

@app.route('/client2')
def client2():
    return render_template('client.html', username="Client 2")

@socketio.on('message')
def handle_message(data):
    username = data['username']
    msg = data['message']
    print(f"{username}: {msg}")
    emit('message', {'username': username, 'message': msg}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
