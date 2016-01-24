# -*- coding: utf-8 -*-

# python imports
import uuid as _id


class GenerateUUID(object):
	def __init__(self, abc=None):
		if abc is None:
			abc = list(	"0123456789"
					"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
					"abcdefghijklmnopqrstuvwxyz"
					"-_"
					)
			# print(len(abc))
		self.update_abc(abc)

	@property
	def uuid_lenght(self):
	
		return  len(self._abc)
	
	def num2str(self,num):
		"""
	        	convert a number to a string, using the given combined data
	        	"""
		# abc = list(	"0123456789"
		# 			"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		# 			"abcdefghijklmnopqrstuvwxyz"
		# 			"-_"
		# 		)

		result = ""
		while num:
		    num, digit = divmod(num, self.uuid_lenght) # len(self._abc)
		    result += self._abc[digit]
		
		return result

	def encode(self, _uuid):
		"""
		encodes a UUID into a string
		"""
		return self.num2str(_uuid.int)

	def update_abc(self, abc):

		get_combined_data = list(sorted(set(abc))) # list(abc)
		self._abc = get_combined_data

	@property
	def _uu(self):
		"""
		get universal unique identification
		"""

		return _uu.uuid4()

	def _uuid(self):
		"""
		generate and return a UUID
		"""

		uuid = self._uu #_uu.uuid4() #get_unique_txnid()

		return self.encode(uuid)


_inst = GenerateUUID()
uuid = _inst._uuid

"""
>>> import gen_uuid
>>> gen_uuid.uuid()
'mWPiqi5z_qQO-lr8L0LLu0'
"""

# native uuid(universal unique identification) generation, callable from uuid module
# import uuid

def get_uuid_txnid():
	"""
	get universal unique identification
	>>> get_uuid_txnid()
	'10719362535681888741'
	"""
	return str(_uu.uuid1().int >> 64)

def get_unique_txnid():
	"""
	get universal unique identification
	>>>  get_unique_txnid()
	'1009a807b4084628a2b727587103f110'
	"""
	return ''.join(str(_uu.uuid4()).split('-'))