from flask import Flask, request
from flask_cors import CORS
from graph_service import *
import graph_route
import logging

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.logger.setLevel(logging.DEBUG)

    graph_service = GraphService()

    app.register_blueprint(graph_route.construct_blueprint(graph_service))

    return app
    