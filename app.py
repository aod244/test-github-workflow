from flask import Flask
"""import flask"""
app = Flask(__name__)
@app.route('/')
def hello():
    """Funkcja lint"""
    return "<h1>Hello WSB! Greetings from Flask!</h1>"
if __name__ == "__main__":
    app.run(debug=True)
