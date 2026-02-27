from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello Azure ! 🚀</h1><p>Déployé via GitHub</p>"

@app.route('/health')
def health():
    return {"status": "ok"}

if __name__ == '__main__':
    app.run(debug=True)