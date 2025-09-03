from flask import Flask

app = Flask(__name__)

@app.route("/")
def say_hello():
    return "Hello, World 2 from Python Docker!"

if __name__ == "__main__":
    # Listen on all interfaces on port 9091 (different from 9090)
    app.run(host="0.0.0.0", port=9091)
