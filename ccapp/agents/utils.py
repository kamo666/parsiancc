import ESL, json, math
from ccapp.models import cdr, aggentt, quueuue
from flask import jsonify
from datetime import datetime, timedelta
from ccapp.mod import fsapi
import time

def get_agent_details(queue, page, per_page):
    ea = fsapi.Callcenterinfo()
    ea.queue = str(queue)
    agent_list = ea.agent2dict()
    tagent = len(agent_list)
    agent_info = []
    e = fsapi.Callcenterinfo()
    e.queue = str(queue)
    member_list = e.member2dict()
    active_agents = 0
    for i in range(tagent):
        res = None
        ress = None
        for sub in member_list:
            if sub['serving_agent'] == agent_list[i]['name']:
               res = sub['cid_number']
               ress = sub['session_uuid']
               break
        if agent_list[i]['status'] == 'Available':
           active_agents +=1
        contact = agent_list[i]['contact']
        extension = contact.split('/')[1].split('@')[0]
        epoch_status_change = agent_list[i]['last_status_change']
        epoch_bridge_start = agent_list[i]['last_bridge_start']
        epoch_bridge_end = agent_list[i]['last_bridge_end']
        last_status_change = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(epoch_status_change)))
        last_bridge_start = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(epoch_bridge_start)))
        last_bridge_end = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(epoch_bridge_end)))
        time0 = datetime.strptime(last_bridge_start, '%Y-%m-%d %H:%M:%S')
        if res != None:
           time1 = datetime.now()
        else:
           time1 = datetime.strptime(last_bridge_end, '%Y-%m-%d %H:%M:%S')
        deltatime0 = str(time1 - time0)
        dtime0 = datetime.strptime(last_status_change, '%Y-%m-%d %H:%M:%S')
        dtime1 = datetime.now()
        deltatime = str(dtime1 - dtime0)
        lost_call1 = cdr.query.filter(cdr.start_stamp > dtime0, cdr.start_stamp <= dtime1).filter(cdr.cc_agent == agent_list[i]['name'])\
                                     .filter(cdr.hangup_cause == 'ORIGINATOR_CANCEL').count()
        lost_call2 = cdr.query.filter(cdr.start_stamp > dtime0, cdr.start_stamp <= dtime1).filter(cdr.cc_agent == agent_list[i]['name'])\
                                     .filter(cdr.hangup_cause == 'NO_ANSWER').count()
        inbound_call = cdr.query.filter(cdr.start_stamp > dtime0, cdr.start_stamp <= dtime1).filter(cdr.cc_agent == agent_list[i]['name']).count()
        outbound_call = cdr.query.filter(cdr.start_stamp > dtime0, cdr.start_stamp <= dtime1).filter(cdr.caller_id_number == extension).count()
        ans = cdr.query.filter(cdr.start_stamp > dtime0, cdr.start_stamp <= dtime1).filter(cdr.cc_agent == agent_list[i]['name'])\
                                     .filter(cdr.hangup_cause == 'NORMAL_CLEARING').count()
        ag = {'name':agent_list[i]['name'], 'extension': extension, 'state': agent_list[i]['state'], 'lost_call':lost_call1+lost_call2,\
              'inbound_call': inbound_call, 'outbound_call': outbound_call, 'answer_call': ans, 'status':  agent_list[i]['status'],\
              'last_status_change_duration': deltatime.split('.')[0], 'last_bridge_duration': deltatime0.split('.')[0], 'active_call': res,\
              'session_uuid': ress }
        agent_info.append(ag)
    agent_real_name = {}
    ag = aggentt.query.all()
    for row in ag:
        agent_real_name[str(row.call_center_agent_uuid)] = str(row.agent_name.encode('utf-8'))
    tagents = len(agent_info)
    totalpages = int(math.ceil(float(tagents)/float(per_page)))
    agent_info_per_page = agent_info[(page-1)*per_page:(page-1)*per_page+per_page]
    ad_agent = {'total_agents': tagents, 'active_agents': active_agents}
    return jsonify(agent_information = agent_info_per_page, agent_uuid_name = agent_real_name,\
                   total_page = totalpages, active_and_total_agents = ad_agent)
