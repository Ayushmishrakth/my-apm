from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def index():
    time.sleep(0.5)  # Simulate work
    return "✅ Hello from your OpenTelemetry APM tool!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

