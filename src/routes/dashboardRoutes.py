from flask import Blueprint, request, Flask
from flask_cors import cross_origin
from flask_restplus import Namespace, Resource

import src.controllers.dashboardController as dashboardController

app = app = Flask(__name__)

dashboard = Blueprint('dashboard', __name__)
ns_report = Namespace('schedule',description='List of operations for TV Schedule')
@ns_report.route(endpoint='/')
@ns_report.doc(responses={200: "OK"})
class DashboardReport(Resource):
	@dashboard.route("/", methods=['GET'])
	def get():
			return dashboardController.report()
	


