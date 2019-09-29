from flask import Flask, render_template
from flask_cors import CORS
from flask_socketio import SocketIO
from flask_socketio import emit
import threading
import JSONtoSQLite
from DB_to_websocket import getDataSnapshot, serializeDataSnapshot

def getData():
    thread = threading.Thread(target=JSONtoSQLite.data_ingest)
    thread.start()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.use_reloader=False
socketio = SocketIO(app, cors_allowed_origins="*")

getData()

@app.route("/")
def home():
    return render_template('index.html')

@socketio.on('request-crew-update')
def handle_request_crew_update():
    data = serializeDataSnapshot(getDataSnapshot())
    emit("crew-update", data)




if __name__ == '__main__':
    socketio.run(app)