import sublime, sublime_plugin
class TaberCommand(sublime_plugin.WindowCommand):
	def close_tab(self, v):
		self.window.focus_view(v)
		self.window.run_command('close')	
	def run(self, what):
		act_was = False
		act = self.window.active_view()
		for v in self.window.views():
			if v.id() != act.id():
				if what=="except":
					self.close_tab(v)
				elif what=="left" and not act_was:
					self.close_tab(v)
				elif what=="right" and act_was:
					self.close_tab(v)
			else:
				act_was = True
		self.window.focus_view(act)
		