from ccapp.models import cdr, aggentt, quueuue
from flask import jsonify
from datetime import datetime, timedelta

def get_tcall_graph(date, qname):
    inn = date
    inn = inn.split('-')
    dtime0 = datetime(int(inn[0]), int(inn[1][1:] if inn[1].startswith('0') else inn[1]), int(inn[2][1:] if inn[2].startswith('0') else inn[2]))
    dtime1 = dtime0 + timedelta(hours=23,minutes=59,seconds=59)
    call_graph = []
    for i in range(0, 24):
        onehours0 = dtime0 + timedelta(hours = i)
        onehours1 = onehours0 + timedelta(minutes = 59, seconds = 59)
        answer_per_hours = cdr.query.filter(cdr.start_stamp >= dtime0, cdr.start_stamp <= dtime1).filter(cdr.cc_queue == qname)\
                                        .filter(cdr.cc_cause == 'answered').filter(cdr.start_stamp >= onehours0, cdr.start_stamp <= onehours1).count()
        lost_per_hours = cdr.query.filter(cdr.start_stamp >= dtime0, cdr.start_stamp <= dtime1).filter(cdr.cc_queue == qname)\
                                        .filter(cdr.cc_cause == 'cancel').filter(cdr.start_stamp >= onehours0, cdr.start_stamp <= onehours1).count()
        tcall_per_hours = {str(i):{"call_answered":answer_per_hours,"call_abandoned":lost_per_hours}}
        call_graph.append(tcall_per_hours)
    return jsonify(total_call_graph = call_graph)
