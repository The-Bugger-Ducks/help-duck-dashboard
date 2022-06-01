from flask import Blueprint, request
from flask_cors import cross_origin

import src.controllers.exampleController as exampleController

example = Blueprint('example', __name__)

@example.route("/", methods=['GET'])
@cross_origin()
def index():
	return exampleController.index()


