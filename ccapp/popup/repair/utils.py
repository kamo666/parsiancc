from ccapp.models import cdr, aggentt, quueuue
from flask import jsonify
from datetime import datetime, timedelta

def get_popup(date, page, per_page):
    inn = date
    inn = inn.split('-')
    dtime0 = datetime(int(inn[0]), int(inn[1][1:] if inn[1].startswith('0') else inn[1]), int(inn[2][1:] if inn[2].startswith('0') else inn[2]))
    dtime1 = dtime0 + timedelta(hours=23,minutes=59,seconds=59)
    popup = cdr.query.filter(cdr.start_stamp >= dtime0, cdr.start_stamp <= dtime1).filter(cdr.digits_dialed.like("%22%#%")).paginate(page=page, per_page = per_page)
    popupt = []
    for row in popup.items:
        a = row.digits_dialed
        Terminal_num = a[2:-1]
        popup1 = {'caller_id_number': row.caller_id_number, 'Terminal_number': row.terminal_number_received, 'Date&Time': row.start_stamp}
        popupt.append(popup1)
    return jsonify(total_page = popup.pages, PopUp=popupt)

def get_popupt(page, per_page):
    popup = cdr.query.filter(cdr.digits_dialed.like("%22%#%")).paginate(page=page, per_page = per_page)
    popupt = []
    for row in popup.items:
        a = row.digits_dialed
        Terminal_num = a[2:-1]
        popup1 = {'caller_id_number' : row.caller_id_number, 'Terminal_number' : row.terminal_number_received, 'Date&Time' : row.start_stamp}
        popupt.append(popup1)
    return jsonify(total_pages = popup.pages, PopUp=popupt)
