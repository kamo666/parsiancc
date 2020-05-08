from flask import Flask, request, Blueprint
from ccapp.popup.repair.utils import get_popup, get_popupt
from ccapp.auth.tokens import token_required

pop = Blueprint('pop', __name__)

@pop.route('/popup', methods=['GET', 'POST'])
@token_required
def getpopup():
    if request.method == "GET":
       page = request.args.get('page', 1, type = int)
       per_page = request.args.get('per_page', 8, type = int)
       return get_popupt(page, per_page)
    else:
       date = request.args.get("date",'')
       page = request.args.get('page', 1, type = int)
       per_page = request.args.get('per_page', 8, type = int)
       return get_popup(date, page, per_page)
