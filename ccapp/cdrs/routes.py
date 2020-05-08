from flask import Flask, request, Blueprint
from ccapp.cdrs.utils import get_cdrs, get_caller_id
from ccapp.auth.tokens import token_required

cdr = Blueprint('cdr', __name__)

@cdr.route('/cdr', methods=['GET', 'POST'])
@token_required
def cdrsFunction():
    if request.method == "GET":
       page = request.args.get('page', 1, type = int)
       per_page = request.args.get('per_page', 8, type = int)
       return get_cdrs(page, per_page)
    else:
       caller_id = request.args.get("CallerID",'')
       page = request.args.get('page', 1, type = int)
       per_page = request.args.get('per_page', 8, type = int)
       return get_caller_id(caller_id, page, per_page)
