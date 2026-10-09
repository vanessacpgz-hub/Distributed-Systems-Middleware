from flask import Flask, jsonify  #[cite: 5]

app = Flask(__name__)  #[cite: 5]

@app.route("/saludo")  #[cite: 5]
def saludo():
    return jsonify({"mensaje": "Hola desde el servidor REST"})  #[cite: 5]

if __name__ == "__main__":  #[cite: 5]
    app.run(port=5000)  #[cite: 5, 6]
