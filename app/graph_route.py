from flask import Blueprint, Response, request

def construct_blueprint(graph_service):
    bp_graph = Blueprint("bp_graph", __name__)
    
    @bp_graph.route('/comparisons', methods=['POST'])
    def save_comparsions():
      body = request.get_json()
      if (graph_service.save_comparisons(body)):
        return Response(status=201)
      return Response(status=400)

    @bp_graph.route('/path')
    def get_path():
      origin = request.args.get('origin')
      destination = request.args.get('destination')
      graph_service.get_path(origin, destination)
      return Response(status=200)

    return bp_graph