from flask import Flask, request, Blueprint
from ccapp.callreport.avgcall.utils import get_acall_graph
from ccapp.auth.tokens import token_required

avg = Blueprint('avg', __name__)

@avg.route('/callcenteraveragegraph', methods=['GET', 'POST'])
@token_required
def callcentertagraphFunction():
    if request.method == "GET":
       return {'error': 'please POST date and queue_name!'}
    else:
       date = request.args.get("date",'')
       qname = request.args.get('queue_name', '')
       return get_acall_graph(date, qname)
