import codewave_core.cmd_finder as cmd_finder

class Context():
	def __init__(self,codewave):
		self.codewave = codewave
		self.nameSpaces = []
	
	def addNameSpace(self,name):
		if name not in self.nameSpaces :
			self.nameSpaces.append(name)
			self._namespaces = None
	def addNamespaces(self,spaces):
		if spaces :
			if isinstance(spaces, str):
				spaces = [spaces]
			for space in spaces :
				self.addNameSpace(space)
	def removeNameSpace(self,name):
		self.nameSpaces = [n for n in self.nameSpaces.filter if n != name]

	def getNameSpaces(self,):
		if self._namespaces is None:
			npcs = ['core'].concat(self.nameSpaces)
			if self.parent is not None:
				npcs += self.parent.getNameSpaces()
			self._namespaces = util.unique(npcs)
		return self._namespaces
	def getCmd(self,cmdName,nameSpaces = []):
		finder = self.getFinder(cmdName,nameSpaces)
		return finder.find()
	def getFinder(self,cmdName,nameSpaces = []):
		return cmd_finder.CmdFinder(cmdName, {
			namespaces: nameSpaces
			useDetectors: self.isRoot()
			codewave: self.codewave
			parentContext: self
		})
	def isRoot(self):
		return not self.parent is not None
	def wrapComment(self,str):
		cc = self.getCommentChar()
		if '%s' in cc:
			return cc.replace('%s',str)
		else:
			return cc + ' ' + str + ' ' + cc
	def wrapCommentLeft(self,str = ''):
		cc = self.getCommentChar()
		i = cc.index('%s') if '%s' in cc else None
		if i is not None:
			return cc[0:i] + str
		else:
			return cc + ' ' + str
	def wrapCommentRight(self,str = ''):
		cc = self.getCommentChar()
		i = cc.index('%s') if '%s' in cc else None
		if i is not None:
			return str + cc[i+2:]
		else:
			return str + ' ' + cc
	def getCommentChar(self):
		if self.commentChar is not None:
			return self.commentChar
		cmd = self.getCmd('comment')
		if cmd is not None:
			res = cmd.result()
			if res is not None:
				res = res.replace('~~content~~','%s')
				if self.process is not None:
					self.commentChar = res
				return res
		return '<!-=1 %s -=1>'