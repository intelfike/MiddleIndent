import sublime
import sublime_plugin


class MiddleIndentCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# 一番右にあるカーソル位置を取得する
		right_max = 0
		for region in self.view.sel():
			cursor_pos = region.b
			_, left = self.view.rowcol(cursor_pos)
			if left > right_max:
				right_max = left

		# すべてのカーソル位置に、一番右にあるカーソル位置に合わせて移動するようスペースを入れる
		for region in self.view.sel():
			cursor_pos = region.b
			_, left = self.view.rowcol(cursor_pos)
			for n in range(left, right_max):
				self.view.insert(edit, cursor_pos, " ")