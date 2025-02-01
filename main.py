from flask import Flask, request, jsonify
app = Flask(__name__)
#app = FastAPI()

@app.get("/")
def read_root():
    return "Hello, World!"
