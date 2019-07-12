import sys, re

class ele:
	def __init__(self, tag, value=''):
		self.tag = tag
		self.value = value
		self.children = []    

	def ch(self, child):
		self.children.append(child)
	
	def pr(self, depth):
		depth += 1
		ident = '   '*depth
		if self.value :
			print ident,"<"+self.tag+">"+self.value+"</"+self.tag+">"
		else:
			print ident,"<"+self.tag+">"
			if len(self.children) > 0:
				for child in self.children:
					child.pr(depth)
			print ident,"</"+self.tag+">"
			
	def prStr(self, depth):
		depth += 1
		ident = '   '*depth
		if self.value :
			print ident,"<"+self.tag+">"
		else:
			print ident,"<"+self.tag+">"
			if len(self.children) > 0:
				for child in self.children:
					child.prStr(depth)


class tree:
	def __init__(self, tag, conf, children):
		self.tag = tag
		self.conf = conf
		self.children = children
				
	def printXML(self,depth=0):
		print "<"+self.tag, self.conf+">"
		for child in self.children:
			child.pr(depth)
		print "</"+self.tag+">"
		
	def xmlStr(self,depth=0):
		print "<"+self.tag+">"
		for child in self.children:
			child.prStr(depth)
		
		
	
file_name = "C:/Users/jmelinovskis/Desktop/file2.xml"

my = open(file_name)
inp = my.read()
my.close()

str = inp.replace('\n','')
obj = re.findall(r'(.*?>)(.*?)<', str, re.M)

data = []

for item in obj:	
	if item[0][4] != "?":
		tag = item[0]
		data.append([tag[:-1],item[1]])		

dom = []
lastOpen = []
	
for item in data:
	if item[1] == '':
		del item[1]
		if item[0][0] != '/':
			thisCh = ele(item[0])
			if len(lastOpen) > 0:
				lastOpen[-1].ch(thisCh)
			else:
				dom.append(thisCh)
			lastOpen.append(thisCh)
		else:
			del lastOpen[-1]
			del item[0]
	else: 
		thisCh = ele(item[0],item[1])
		if len(lastOpen) > 0:
			lastOpen[-1].ch(thisCh)
		lastOpen.append(thisCh)
			
if len(dom) == 1:
	obj = re.findall('(.*?)\s(.*)', dom[0].tag)
	fix = re.findall('.*?<(.*)',obj[0][0])
	if len(fix) > 0:
		XML = tree(fix[0], obj[0][1], dom[0].children)
	else:	
		XML = tree(obj[0][0], obj[0][1], dom[0].children)
else:
	print 'Could not distinguish Head'
	
#XML.xmlStr()
XML.printXML()










