from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    # Get query parameter "name", default to "Guest"
    name = request.args.get("name", "Guest")
    return f"Hello, World 4! Welcome, {name}."

if __name__ == "__main__":
    # Listen on port 9093
    app.run(host="0.0.0.0", port=9093)
