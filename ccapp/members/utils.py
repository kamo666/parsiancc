import ESL, json, math
from ccapp.models import cdr, aggentt, quueuue
from flask import jsonify
from datetime import datetime, timedelta
from ccapp.mod import fsapi
import time

def get_member_details(queue, page, per_page):
    ea = fsapi.Callcenterinfo()
    ea.queue = str(queue)
    member_list = ea.member2dict()
    tmember = len(member_list)
    member_info = []
    e = fsapi.Callcenterinfo()
    e.queue = str(queue)
    agent_list = e.agent2dict()
    ett = 0
    for i in range(tmember):
        if member_list[i]['state'] != 'Abandoned':
           ett += 1
           res = None
           for sub in agent_list:
               if sub['name'] == member_list[i]['serving_agent']:
                  res = sub['contact'].split('/')[1].split('@')[0]
                  break
           member_callerID = member_list[i]['cid_number']
           epoch_joined = member_list[i]['joined_epoch']
           epoch_bridge = member_list[i]['bridge_epoch']
           joined_epoch = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(epoch_joined)))
           bridge_epoch = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(epoch_bridge)))
           time0 = datetime.strptime(joined_epoch, '%Y-%m-%d %H:%M:%S')
           if epoch_bridge == '0':
              time1 = datetime.now()
           else:
              time1 = datetime.strptime(bridge_epoch, '%Y-%m-%d %H:%M:%S')
           deltatime0 = str(time1 - time0)
           me = {'caller_ID_number':member_list[i]['cid_number'], 'waiting_time_duration': deltatime0.split('.')[0], 'agent_extension': res}
           member_info.append(me)
    tmembers = len(member_info)
    totalpages = int(math.ceil(float(tmembers)/float(per_page)))
    member_info_per_page = member_info[(page-1)*per_page:(page-1)*per_page+per_page]
    return jsonify(member_information = member_info_per_page, number_of_callers = str(ett), total_pages = totalpages)
