class Editor():
	def __init__(self):
		self.namespace = None
		self._lang = None
		
	def bindedTo(self,codewave):
		pass

	@property
	def text(self):
		raise NotImplementedError
	@text.setter
	def text(self, val):
		raise NotImplementedError
	def textCharAt(self,pos):
		raise NotImplementedError
	def textLen(self):
		raise NotImplementedError
	def textSubstr(self,start, end):
		raise NotImplementedError
	def insertTextAt(self,text, pos):
		raise NotImplementedError
	def spliceText(self,start, end, text):
		raise NotImplementedError
	def getCursorPos(self):
		raise NotImplementedError
	def setCursorPos(self,start, end = None):
		raise NotImplementedError
	def beginUndoAction(self):
		pass
	def endUndoAction(self):
		pass
	def getLang(self):
		return self._lang
	def setLang(self,val):
		self._lang = val
	def getEmmetContextObject(self):
		return None
	def allowMultiSelection(self):
		return False
	def setMultiSel(self,selections):
		raise NotImplementedError
	def getMultiSel(self):
		raise NotImplementedError
	def canListenToChange(self):
		return False
	def addChangeListener(self,callback):
		raise NotImplementedError
	def removeChangeListener(self,callback):
		raise NotImplementedError
	
	def applyReplacements(self,replacements):
		selections = []
		offset = 0
		for repl in replacements:
			repl.applyOffset(offset)
			repl.applyToEditor(self)
			offset += repl.offsetAfter()
			
			selections += repl.selections
		self.applyReplacementsSelections(selections)
			
	def applyReplacementsSelections(self,selections):
		if len(selections) > 0:
			if self.allowMultiSelection():
				self.setMultiSel(selections)
			else:
				self.setCursorPos(selections[0].start,selections[0].end)