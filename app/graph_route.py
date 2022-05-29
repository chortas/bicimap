from flask import Blueprint, Response, request

def construct_blueprint(graph_service):
    bp_graph = Blueprint("bp_graph", __name__)
    
    @bp_graph.route('/comparisons', methods=['POST'])
    def save_comparsions():
      body = request.get_json()
      graph_service.save_comparisons(body)
      return Response(status=201)

    @bp_graph.route('/path')
    def get_path():
      body = request.get_json()
      graph_service.get_path(body)
      return Response(status=200)

    return bp_graph