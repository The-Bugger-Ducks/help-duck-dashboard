from flask import Flask, jsonify
from flask_restful import Resource
from flask_restplus import Api

import src.controllers.dashboardController as dashboardController

app = Flask(__name__)
api = Api(app, version='1.0', title='Dashboard Micro service',
    description='Micro service for dashboard system visualization ',
)

@api.route('/dashboard/')
class MyResource(Resource):
    @app.route('/dashboard/')
    def get():
        return dashboardController.report()

if __name__ == '__main__':
	app.run(debug=True)
