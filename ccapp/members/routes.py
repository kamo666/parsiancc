from flask import Flask, request, Blueprint
from ccapp.members.utils import get_member_details
from ccapp.auth.tokens import token_required

member = Blueprint('member', __name__)

@member.route('/callcentermemberinfo', methods=['POST'])
@token_required
def callcentermemberinfoFunction():
    qname = request.args.get('queue_name', '')
    page = request.args.get('page', 1, type = int)
    per_page = request.args.get('per_page', 8, type = int)
    return get_member_details(qname, page, per_page)
