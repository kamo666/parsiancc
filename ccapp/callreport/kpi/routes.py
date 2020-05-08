from flask import Flask, request, Blueprint
from ccapp.callreport.kpi.utils import get_kpi
from ccapp.auth.tokens import token_required

kpi = Blueprint('kpi', __name__)

@kpi.route('/callcenterkpi', methods=['POST'])
@token_required
def callcenterkpiFunction():
    date = request.args.get("date",'')
    qname = request.args.get('queue_name', '')
    page = request.args.get('page', 1, type = int)
    per_page = request.args.get('per_page', 8, type = int)
    return get_kpi(date, qname, page, per_page)
