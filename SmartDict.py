class SmartDict(dict):
  __author__ = "MacHacker"
  __licence__ = "GNU v3.0"
	"""
	This is just like a normal dictionary except you don't need to define keys before adding values
	E.G.
		
		sd = SmartDict()
		sd['x']['y']['z'] = [1,2,3,4,5]
		print sd #=> SmartDict({'x': SmartDict({'y': SmartDict({'z': [1, 2, 3, 4, 5]})})})
		##################################################################################
		sd = SmartDict()
		for i in range(20):
			if i%2:
				sd['odd', list].append(i)
			else:
				sd['even', list].append(i)
		print sd #=> SmartDict({'even': [0, 2, 4, 6, 8, 10, 12, 14, 16, 18], 'odd': [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]})
	"""
	def __init__(self, dict=None):
		super(SmartDict, self).__init__(dict if dict else {})

	def __repr__(self):
		return "{}({})".format(self.__class__.__name__, super(SmartDict, self).__repr__())
	def __setitem__(self, item, value):
		setitem = super(SmartDict, self).__setitem__
		if item not in self.keys():
			setitem(item, value)

	def __getitem__(self, item):
		getitem = super(SmartDict, self).__getitem__
		datatype = self.__class__
		if type(item) is tuple:
			item, datatype = item
		if item not in self.keys():
			self[item] = datatype()
return getitem(item)
