import cmd2dict

class Callcenterinfo:
      def __init__(self):
          self.queue = ""
          self.agentcmd = "callcenter_config queue list agents"
          self.membercmd = "callcenter_config queue list members"
          self.queuecmd = "callcenter_config queue list"
      def queue2dict(self):
	  cmd = self.queuecmd + " " + str(self.queue)
          queue_list = cmd2dict.cmd2dict(cmd)
          return queue_list

      def agent2dict(self):
          cmd = self.agentcmd + " " + str(self.queue)
          agent_list = cmd2dict.cmd2dict(cmd)
          return agent_list

      def member2dict(self):
          cmd = self.membercmd + " " + str(self.queue)
          member_list = cmd2dict.cmd2dict(cmd)
          return member_list
