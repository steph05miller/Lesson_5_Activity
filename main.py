import os
import time
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return jsonify(epoch_time=int(time.time()))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

