from flask import Flask, jsonify
from flask_cors import CORS

from src.routes.exampleRoutes import example

app = Flask(__name__)

app.register_blueprint(example, url_prefix='/example')

@app.route('/')
def test():
  jsonTest = {"status": "API Online"}
  return jsonify(jsonTest)

if __name__ == '__main__':
	app.run(debug=True)