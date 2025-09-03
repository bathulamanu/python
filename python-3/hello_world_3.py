from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    name = request.args.get("name", "Guest")
    return f"Hello, World 3! Welcome, {name}."

if __name__ == "__main__":
    # Listen on all interfaces on port 9092 (different from 9090, 9091)
    app.run(host="0.0.0.0", port=9092)
