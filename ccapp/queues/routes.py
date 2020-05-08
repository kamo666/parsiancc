from flask import Flask, request, Blueprint
from ccapp.queues.utils import get_queue_details
from ccapp.auth.tokens import token_required

queue = Blueprint('queue', __name__)

@queue.route('/callcenterqueueinfo', methods=['POST'])
@token_required
def callcenterqueueinfoFunction():
    date = request.args.get('date', '')
    page = request.args.get('page', 1, type = int)
    per_page = request.args.get('per_page', 8, type = int)
    return get_queue_details(date, page, per_page)
