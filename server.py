from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit
from DB_to_websocket import getDataSnapshot, serializeDataSnapshot
log = open("server_log.txt", 'w')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)

@socketio.on('request-crew-update')
def handle_request_crew_update():
    emit("crew-update", serializeDataSnapshot(getDataSnapshot()))

@socketio.on('message')
def handle_message(message):
    log.write("recieved message from client: ", message)

