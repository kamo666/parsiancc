import ESL, json, math
from ccapp.models import cdr, aggentt, quueuue
from flask import jsonify
from datetime import datetime, timedelta
from ccapp.mod import fsapi

def get_queue_details(date, page, per_page):
    inn = date
    inn = inn.split('-')
    dtime0 = datetime(int(inn[0]), int(inn[1][1:] if inn[1].startswith('0') else inn[1]), int(inn[2][1:] if inn[2].startswith('0') else inn[2]))
    dtime1 = dtime0 + timedelta(hours=23,minutes=59,seconds=59)
    ea = fsapi.Callcenterinfo()
    queue_list = ea.queue2dict()
    tqueue = len(queue_list)
    queue_info = []
    qu = quueuue.query.all()
    for i in range(tqueue):
        Q_c = cdr.query.filter(cdr.start_stamp > dtime0, cdr.start_stamp <= dtime1).filter(cdr.cc_queue == queue_list[i]['name'])\
                              .filter(cdr.cc_cause == 'cancel').count()
        eg = fsapi.Callcenterinfo()
        eg.queue = str(queue_list[i]['name'])
        agent_list = eg.agent2dict()
        tagent = len(agent_list)
        answer_call = 0
        noanswer_call = 0
        lost_call = 0
        for k in range(tagent):
            lost_call1 = cdr.query.filter(cdr.start_stamp > dtime0, cdr.start_stamp <= dtime1).filter(cdr.cc_agent == agent_list[k]['name'])\
                                          .filter(cdr.hangup_cause == 'ORIGINATOR_CANCEL').count()
            lost_call2 = cdr.query.filter(cdr.start_stamp > dtime0, cdr.start_stamp <= dtime1).filter(cdr.cc_agent == agent_list[k]['name'])\
                                          .filter(cdr.hangup_cause == 'NO_ANSWER').count()
            ans = cdr.query.filter(cdr.start_stamp > dtime0, cdr.start_stamp <= dtime1).filter(cdr.cc_agent == agent_list[k]['name'])\
                                   .filter(cdr.hangup_cause == 'NORMAL_CLEARING').count()
            answer_call += ans
            noanswer_call += lost_call2
            lost_call += lost_call1
        extension = 0
        for row in qu:
            if str(row.call_center_queue_uuid) == str(queue_list[i]['name']):
               extension = row.queue_extension
               break
        e = fsapi.Callcenterinfo()
        e.queue = str(queue_list[i]['name'])
        member_list = e.member2dict()
        tmember = len(member_list)
        ett = 0
        for j in range(tmember):
            if member_list[j]['state'] != 'Abandoned':
               ett += 1
        quu = {'queue_name': queue_list[i]['name'], 'queue_number': extension, 'strategy': queue_list[i]['strategy'], 'number_of_member': str(ett),\
                'total_answered': answer_call, 'total_no_answered': noanswer_call, 'total_lostcall': Q_c, 'total_call': answer_call + Q_c}
        queue_info.append(quu)
    tqueues = len(queue_info)
    totalpages = int(math.ceil(float(tqueues)/float(per_page)))
    queue_info_per_page = queue_info[(page-1)*per_page:(page-1)*per_page+per_page]
    queue_real_name = {}
    for row in qu:
        queue_real_name[str(row.call_center_queue_uuid)] = str(row.queue_name.encode('utf-8'))
    return jsonify(queue_information = queue_info_per_page, total_queue = tqueues, queue_uuid_name = queue_real_name,\
                   total_page = totalpages)

