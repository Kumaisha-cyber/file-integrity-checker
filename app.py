from flask import Flask, render_template, request, jsonify
import hashlib

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check_file():

    file = request.files["file"]

    file_data = file.read()

    current_hash = hashlib.sha256(file_data).hexdigest()

    return jsonify({
        "message": f"File checked successfully!\nSHA-256 Hash: {current_hash}"
    })


if __name__ == "__main__":
    app.run(debug=True)