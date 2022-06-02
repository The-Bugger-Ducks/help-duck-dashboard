from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api

from src.routes.exampleRoutes import example

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.register_blueprint(example, url_prefix='/example')

@app.route('/')
def test():
  jsonTest = {"status": "API Online"}
  return jsonify(jsonTest)

if __name__ == '__main__':
	app.run(debug=True)