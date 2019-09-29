from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from flask_socketio import emit
import _thread
import JSONtoSQLite
from DB_to_websocket import getDataSnapshot, serializeDataSnapshot
log = open("server_log.txt", 'w')

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('request-crew-update')
def handle_request_crew_update():
    data = serializeDataSnapshot(getDataSnapshot())
    emit("crew-update", data)

_thread.start_new_thread(JSONtoSQLite.data_ingest())


if __name__ == '__main__':
    socketio.run(app)