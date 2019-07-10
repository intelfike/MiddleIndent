import sublime
import sublime_plugin


class MiddleIndentCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		right_max = 0
		for region in self.view.sel():
			cursor_pos = region.b
			_, left = self.view.rowcol(cursor_pos)
			if left > right_max:
				right_max = left

		for region in self.view.sel():
			cursor_pos = region.b
			_, left = self.view.rowcol(cursor_pos)
			for n in range(left, right_max):
				self.view.insert(edit, cursor_pos, " ")