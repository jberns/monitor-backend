from flask import Flask, render_template
from flask_cors import CORS
from flask_socketio import SocketIO
from flask_socketio import send, emit
from DB_to_websocket import getDataSnapshot, serializeDataSnapshot
log = open("server_log.txt", 'w')

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def hello():
    log = open("server_log.txt", 'w')
    log.write("got here")
    log.close()
    return render_template('index.html')

@socketio.on('my event')
def handle_message(message):
    print('received message: ' + message['data'])

@socketio.on('request-crew-update')
def handle_request_crew_update():
    data = serializeDataSnapshot(getDataSnapshot())
    print(data)
    emit("crew-update", data)

@socketio.on('message')
def handle_message(message):
    log.write("recieved message from client: ", message)

if __name__ == '__main__':
    socketio.run(app)