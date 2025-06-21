from flask import Flask
import socket
import psutil
import platform

app = Flask(__name__)

@app.route("/")
def system_info():
    return {
        "hostname": socket.gethostname(),
        "cpu_percent": psutil.cpu_percent(),
        "memory_percent": psutil.virtual_memory().percent,
        "platform": platform.platform()
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
