from ccapp.models import cdr, aggentt, quueuue
from flask import jsonify
from datetime import datetime, timedelta
import time

def get_kpi(date, qname, page, per_page):
    qname = str(qname)
    inn = date
    inn = inn.split('-')
    dtime0 = datetime(int(inn[0]), int(inn[1][1:] if inn[1].startswith('0') else inn[1]), int(inn[2][1:] if inn[2].startswith('0') else inn[2]))
    dtime1 = dtime0 + timedelta(hours=23,minutes=59,seconds=59)
    Qtimes = cdr.query.filter(cdr.start_stamp >= dtime0, cdr.start_stamp <= dtime1).filter(cdr.cc_queue == qname).paginate(page=page, per_page = per_page)
    Qtimes_c = cdr.query.filter(cdr.start_stamp >= dtime0, cdr.start_stamp <= dtime1).filter(cdr.cc_queue == qname).filter(cdr.cc_cause == 'cancel')
    Qtimes_a = cdr.query.filter(cdr.start_stamp >= dtime0, cdr.start_stamp <= dtime1).filter(cdr.cc_queue == qname).filter(cdr.cc_cause == 'answered')
    w = 0
    a = 0
    mw = 0
    ma = 0
    tQtimes_c = 0
    tQtimes_a = 0
    for row in Qtimes_c:
        tQtimes_c += 1
        w += row.duration
        if row.duration > mw:
           mw = row.duration
    for row in Qtimes_a:
        tQtimes_a += 1
        w += row.waitsec
        a += row.duration - row.waitsec
        if row.waitsec > mw:
           mw = row.waitsec
        if row.duration - row.waitsec > ma:
           ma = row.duration - row.waitsec
    total_call_in_q = tQtimes_c + tQtimes_a
    if total_call_in_q == 0:
       total_call_in_q = 1
    if tQtimes_a == 0:
       tQtimes_a = 1
    ww = time.strftime('%H:%M:%S', time.gmtime(w/total_call_in_q))
    aa = time.strftime('%H:%M:%S', time.gmtime(a/tQtimes_a))
    mww = time.strftime('%H:%M:%S', time.gmtime(mw))
    maa = time.strftime('%H:%M:%S', time.gmtime(ma))
    timehist_of_queue = {'Avrage_Wait_Time' : ww ,'Avrage_Call_Time': aa ,'Maximum_Wait_time': mww, 'Maximum_Call_Time': maa}
    return jsonify(KPI = timehist_of_queue, total_pages = Qtimes.pages, Queue_CDR = [b.serialize for b in Qtimes.items])
