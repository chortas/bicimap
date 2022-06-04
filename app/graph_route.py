from flask import Blueprint, Response, request, render_template_string

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
      try:
        origin = request.args.get('origin') + ', Buenos Aires'
        destination = request.args.get('destination') + ', Buenos Aires'
        path = graph_service.get_path(origin, destination)
        return render_template_string(path)
      except Exception as e:
        print(e)
        return Response(status=400)
    return bp_graph