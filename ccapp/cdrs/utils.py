from ccapp.models import cdr, aggentt, quueuue
from flask import jsonify

def get_cdrs(page, per_page):
    cdrs = cdr.query.paginate(page=page, per_page = per_page)
    return jsonify(total_pages = cdrs.pages, cdrs=[b.serialize for b in cdrs.items])

def get_caller_id(caller_id, page, per_page):
    callerID =  cdr.query.filter_by(caller_id_number = caller_id).paginate(page=page, per_page = per_page)
    return jsonify(total_pages = callerID.pages, callerID=[b.serialize for b in callerID.items])
