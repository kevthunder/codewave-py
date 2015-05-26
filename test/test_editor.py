
import codewave_core.text_parser as text_parser
import codewave_core.util as util

class TestEditor(text_parser.TextParser):
	def __init__(self, text):
		self._text = text
		self.namespace = 'test'
		self.changeListeners = []
		self.selections = []
		self._lang = None
	def getCursorPos(self):
		return self.selections[0]
	def allowMultiSelection(self):
		return True
	def setCursorPos(self,start, end = None):
		if end is None :
			end = start
		self.selections = [util.Pos(start, end)]
	def setMultiSel(self,selections):
		self.selections = list(map(lambda s: s.copy(), selections))
	def getMultiSel(self):
		return self.selections
	def canListenToChange(self):
		return True
	def onAnyChange(self):
		for callback in self.changeListeners :
			callback()
	def addChangeListener(self,callback):
		self.changeListeners.append(callback)
	def removeChangeListener(self,callback):
		self.changeListeners.remove(callback)