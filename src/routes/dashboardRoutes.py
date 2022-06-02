from flask import Blueprint, request
from flask_cors import cross_origin

import src.controllers.dashboardController as dashboardController

dashboard = Blueprint('dashboard', __name__)

@dashboard.route("/report", methods=['GET'])
@cross_origin()
def index():
	return dashboardController.report()


