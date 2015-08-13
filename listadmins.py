__version__ = '1.0.0'
__author__  = 'ListAdmins'

import b3, re, time
import b3.events

class ListAdmins(b3.plugin.Plugin):
	_adminPlugin = None
	
	def startup(self):
		"""\
		Initialize plugin settings
		"""

		# get the admin plugin so we can register commands
		self._adminPlugin = self.console.getPlugin('admin')
		if not self._adminPlugin:
			# something is wrong, can't start without admin plugin
			self.error('Could not find admin plugin')
			return False
    
		# register our commands
		if 'commands' in self.config.sections():
			for cmd in self.config.options('commands'):
			level = self.config.get('commands', cmd)
			sp = cmd.split('-')
			alias = None
			if len(sp) == 2:
				cmd, alias = sp

			func = self.getCmd(cmd)
			if func:
				self._adminPlugin.registerCommand(self, cmd, level, func, alias)

		self.debug('Started')
		
		
	def getCmd(self, cmd):
		cmd = 'cmd_%s' % cmd
		if hasattr(self, cmd):
			func = getattr(self, cmd)
			return func

		return None

	def onEvent(self, event):
		"""\
		Handle intercepted events
		"""



	def get_lstadminsstats(self, name):
		s = lstadminsstats()
		list = 'select * from groups join clients where level >= 20' % (self.clients_table,name)
		cursor = self.query(list)
		if cursor and (cursor.rowcount > 0):
			r = cursor.getRow()
			s.id = r['id']
			s.guid = r['guid']
			s.name = r['name']
			s.mask_level = r['mask_level']
			return s
	def cmd_listadmins(self,data,client):
		"""\
		[<name>] - list of admins
		"""
		liststats = self.get_lstadminsstats(id,name,level)
		if not data:
			message = '^3ListAdmins: ^7%s' % (liststats.id, liststats.Name, liststats.level)
			cmd.sayLoudOrPM(client, message)
			return




