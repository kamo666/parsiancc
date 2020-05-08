from flask import Flask, request, Blueprint
from ccapp.callreport.graph.utils import get_tcall_graph
from ccapp.auth.tokens import token_required

graph = Blueprint('graph', __name__)

@graph.route('/callcentercallgraph', methods=['GET', 'POST'])
@token_required
def callcentertcgraphFunction():
    if request.method == "GET":
       return {'error': 'please POST date and queue_name!'}
    else:
       date = request.args.get("date",'')
       qname = request.args.get('queue_name', '')
       return get_tcall_graph(date, qname)
