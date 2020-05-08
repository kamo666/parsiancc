import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ccapp import db
from datetime import datetime

class quueuue(db.Model):
    __bind_key__ = 'fusionpbx'
    __tablename__ = 'v_call_center_queues'
    call_center_queue_uuid = db.Column(db.String(250),primary_key=True)
    domain_uuid = db.Column(db.String(250))
    dialplan_uuid = db.Column(db.String(250))
    queue_name = db.Column(db.String(250))
    queue_extension = db.Column(db.String(250))
    queue_strategy = db.Column(db.String(250))
    queue_moh_sound = db.Column(db.String(250))
    queue_record_template = db.Column(db.String(250))
    queue_time_base_score = db.Column(db.String(250))
    queue_max_wait_time = db.Column(db.Integer)
    queue_max_wait_time_with_no_agent = db.Column(db.Integer)
    queue_max_wait_time_with_no_agent_time_reached = db.Column(db.Integer)
    queue_tier_rules_apply = db.Column(db.String(250))
    queue_tier_rule_wait_second = db.Column(db.Integer)
    queue_tier_rule_no_agent_no_wait = db.Column(db.String(250))
    queue_timeout_action = db.Column(db.String(250))
    queue_discard_abandoned_after = db.Column(db.Integer)
    queue_abandoned_resume_allowed = db.Column(db.String(250))
    queue_tier_rule_wait_multiply_level = db.Column(db.String(250))
    queue_cid_prefix = db.Column(db.String(250))
    queue_announce_sound = db.Column(db.String(250))
    queue_announce_frequency = db.Column(db.Integer)
    queue_cc_exit_keys = db.Column(db.String(250))
    queue_description = db.Column(db.String(250))     

    @property
    def serialize(self):
        return {
             'call_center_queue_uuid' : self.call_center_queue_uuid,
             'domain_uuid' : self.domain_uuid,
             'dialplan_uuid' : self.dialplan_uuid,
             'queue_name' : self.queue_name,
             'queue_extension' : self.queue_extension,
             'queue_strategy' : self.queue_strategy,
             'queue_moh_sound' : self.queue_moh_sound,
             'queue_record_template' : self.queue_record_template,
             'queue_time_base_score' : self.queue_time_base_score,
             'queue_max_wait_time' : self.queue_max_wait_time,
             'queue_max_wait_time_with_no_agent' : self.queue_max_wait_time_with_no_agent,
             'queue_max_wait_time_with_no_agent_time_reached' : self.queue_max_wait_time_with_no_agent_time_reached,
             'queue_tier_rules_apply' : self.queue_tier_rules_apply,
             'queue_tier_rule_wait_second' : self.queue_tier_rule_wait_second,
             'queue_tier_rule_no_agent_no_wait' : self.queue_tier_rule_no_agent_no_wait,
             'queue_timeout_action' : self.queue_timeout_action,
             'queue_discard_abandoned_after' : self.queue_discard_abandoned_after,
             'queue_abandoned_resume_allowed' : self.queue_abandoned_resume_allowed,
             'queue_tier_rule_wait_multiply_level' : self.queue_tier_rule_wait_multiply_level,
             'queue_cid_prefix' : self.queue_cid_prefix,
             'queue_announce_sound' : self.queue_announce_sound,
             'queue_announce_frequency' : self.queue_announce_frequency,
             'queue_cc_exit_keys' : self.queue_cc_exit_keys,
             'queue_description' : self.queue_description,
        }

class aggentt(db.Model):
    __bind_key__ = 'fusionpbx'
    __tablename__ = 'v_call_center_agents'
    call_center_agent_uuid = db.Column(db.String(250),primary_key=True)
    domain_uuid = db.Column(db.String(250))
    user_uuid = db.Column(db.String(250))
    agent_name = db.Column(db.String(250))
    agent_type = db.Column(db.String(250))
    agent_call_timeout = db.Column(db.Integer)
    agent_id = db.Column(db.String(250))
    agent_password = db.Column(db.String(250))
    agent_contact = db.Column(db.String(250))
    agent_status = db.Column(db.String(250))
    agent_logout = db.Column(db.String(250))
    agent_max_no_answer = db.Column(db.Integer)
    agent_wrap_up_time = db.Column(db.Integer)
    agent_reject_delay_time = db.Column(db.Integer)
    agent_busy_delay_time = db.Column(db.Integer)
    agent_no_answer_delay_time = db.Column(db.String(250))
    
    @property
    def serialize(self):
        return {
            'call_center_agent_uuid': self.call_center_agent_uuid,
            'domain_uuid': self.domain_uuid,
            'user_uuid': self.user_uuid,
            'agent_name': self.agent_name,
            'agent_type': self.agent_type,
            'agent_call_timeout': self.agent_call_timeout,
            'agent_id': self.agent_id,
            'agent_password': self.agent_password,
            'agent_contact': self.agent_contact,
            'agent_status': self.agent_status,
            'agent_logout': self.agent_logout,
            'agent_max_no_answer': self.agent_max_no_answer,
            'agent_wrap_up_time': self.agent_wrap_up_time,
            'agent_reject_delay_time': self.agent_reject_delay_time,
            'agent_busy_delay_time': self.agent_busy_delay_time,
            'agent_no_answer_delay_time': self.agent_no_answer_delay_time,
        }
             
class cdr(db.Model):
    __tablename__ = 'cdr_table_a_leg'
    #__tablename__ = 'cdr'
    caller_id_name = db.Column(db.String(250), nullable=False)
    caller_id_number = db.Column(db.Integer)
    destination_number = db.Column(db.String(250))
    context  = db.Column(db.String(250), nullable=False)
    start_stamp = db.Column(db.String(250), primary_key=True)
    answer_stamp = db.Column(db.String(250))
    end_stamp = db.Column(db.String(250))
    duration = db.Column(db.Integer)
    billsec = db.Column(db.Integer)
    hangup_cause = db.Column(db.String(250))
    uuid = db.Column(db.String(250))
    bleg_uuid = db.Column(db.String(250))
    account_code = db.Column(db.String(250))
    cc_queue = db.Column(db.String(250))
    cc_agent = db.Column(db.String(250))
    cc_cause = db.Column(db.String(250))
    answersec = db.Column(db.Integer)
    waitsec = db.Column(db.Integer)
    progresssec = db.Column(db.Integer)
    hold_accum_seconds = db.Column(db.Integer)
    cc_side = db.Column(db.String(250))
    cc_agent_bridged = db.Column(db.String(250))
    hangup_after_bridge = db.Column(db.String(250))
    current_application = db.Column(db.String(250))
    transfer_history = db.Column(db.String(250))
    ivr_menu_status = db.Column(db.String(250))
    from_user_exists = db.Column(db.String(250))
    user_exists = db.Column(db.String(250))
    direction = db.Column(db.String(250))
    record_ms = db.Column(db.Integer)
    digits_dialed = db.Column(db.Integer)
    bridge_channel = db.Column(db.String(250))
    terminal_number_received = db.Column(db.Integer)    

    @property
    def serialize(self):
        return {
            'caller_id_name': self.caller_id_name,
            'caller_id_number': self.caller_id_number,
            'destination_number': self.destination_number,
            'context': self.context,
            'start_stamp': self.start_stamp,
            'answer_stamp': self.answer_stamp,
            'end_stamp': self.end_stamp,
            'duration': self.duration,
            'billsec': self.billsec,
            'hangup_cause': self.hangup_cause,
            'uuid': self.uuid,
            'bleg_uuid': self.bleg_uuid,
            'account_code': self.account_code,
            'cc_queue': self.cc_queue,
            'cc_agent': self.cc_agent,
            'cc_cause': self.cc_cause,
            'answersec': self.answersec,
            'waitsec': self.waitsec,
            'progresssec': self.progresssec,
            'hold_accum_seconds': self.hold_accum_seconds,
            'cc_side': self.cc_side,
            'cc_agent_bridged': self.cc_agent_bridged,
            'hangup_after_bridge': self.hangup_after_bridge,
            'current_application': self.current_application,
            'transfer_history': self.transfer_history,
            'ivr_menu_status': self.ivr_menu_status,
            'from_user_exists': self.from_user_exists,
            'user_exists': self.user_exists,
            'direction': self.direction,
            'record_ms': self.record_ms,
            'digits_dialed': self.digits_dialed,
            'bridge_channel': self.bridge_channel,
            'terminal_number_received': self.terminal_number_received,
        }
