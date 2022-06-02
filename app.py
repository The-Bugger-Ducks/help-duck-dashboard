from flask import Flask, jsonify

from src.routes.dashboardRoutes import dashboard

app = Flask(__name__)

app.register_blueprint(dashboard, url_prefix='/dashboard')

@app.route('/')
def test():
  jsonTest = {"status": "API Online"}
  return jsonify(jsonTest)

if __name__ == '__main__':
	app.run(debug=True)