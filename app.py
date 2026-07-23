from flask import Flask, render_template, request, jsonify
import hashlib

app = Flask(__name__)

original_hash = None


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check_file():

    global original_hash

    file = request.files["file"]

    file_data = file.read()

    current_hash = hashlib.sha256(file_data).hexdigest()

    if original_hash is None:

        original_hash = current_hash

        return jsonify({
            "message": "ORIGINAL HASH SAVED\n\nFILE INTEGRITY: SAFE\n\nSHA-256 Hash: " + current_hash
        })

    elif current_hash == original_hash:

        return jsonify({
            "message": "FILE INTEGRITY: SAFE\n\nFile has not been modified.\n\nSHA-256 Hash: " + current_hash
        })

    else:

        return jsonify({
            "message": "FILE INTEGRITY: COMPROMISED\n\nFile has been modified!\n\nSHA-256 Hash: " + current_hash
        })


if __name__ == "__main__":
    app.run(debug=True)