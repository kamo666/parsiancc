from ccapp.models import cdr, aggentt, quueuue
from flask import jsonify
from datetime import datetime, timedelta

def get_acall_graph(date, qname):
    inn = date
    inn = inn.split('-')
    dtime0 = datetime(int(inn[0]), int(inn[1][1:] if inn[1].startswith('0') else inn[1]), int(inn[2][1:] if inn[2].startswith('0') else inn[2]))
    dtime1 = dtime0 + timedelta(hours=23,minutes=59,seconds=59)
    acall_graph = []
    for i in range(0, 24):
        onehours0 = dtime0 + timedelta(hours = i)
        onehours1 = onehours0 + timedelta(minutes = 59, seconds = 59)
        Qtimes_a = cdr.query.filter(cdr.start_stamp >= dtime0, cdr.start_stamp <= dtime1).filter(cdr.cc_queue == qname)\
                                        .filter(cdr.cc_cause == 'answered').filter(cdr.start_stamp >= onehours0, cdr.start_stamp <= onehours1)
        Qtimes_c = cdr.query.filter(cdr.start_stamp >= dtime0, cdr.start_stamp <= dtime1).filter(cdr.cc_queue == qname)\
                                        .filter(cdr.cc_cause == 'cancel').filter(cdr.start_stamp >= onehours0, cdr.start_stamp <= onehours1)
        w = 0
        a = 0
        tQtimes_c = 0
        tQtimes_a = 0
        for row in Qtimes_c:
            tQtimes_c += 1
            w += row.duration
        for row in Qtimes_a:
            tQtimes_a += 1
            w += row.waitsec
            a += row.duration - row.waitsec
        total_call_in_q = tQtimes_c + tQtimes_a
        if total_call_in_q == 0:
           total_call_in_q = 1
        if tQtimes_a == 0:
           tQtimes_a = 1
        ww = w/total_call_in_q
        aa = a/tQtimes_a
        tcall_per_hours = {str(i):{"Average_answered_call":aa,"Average_waited_call":ww}}
        acall_graph.append(tcall_per_hours)
    return jsonify(Average_time_call_graph = acall_graph)
