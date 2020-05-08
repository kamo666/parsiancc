from flask import Flask, request, Blueprint
from ccapp.agents.utils import get_agent_details
from ccapp.auth.tokens import token_required

agent = Blueprint('agent', __name__)

@agent.route('/callcenteragentinfo', methods=['POST'])
@token_required
def callcenteragentinfoFunction():
    qname = request.args.get('queue_name', '')
    page = request.args.get('page', 1, type = int)
    per_page = request.args.get('per_page', 8, type = int)
    return get_agent_details(qname, page, per_page)
