#!/usr/bin/env python

# -*- coding: utf-8 -*-

__author__ = "Lasha Gogua"
__version__ = "0.1.0"

# python imports
import uuid as _id


class GenerateUUID(object):
	def __init__(self, abc=None):
		if abc is None:
			abc = list(	"1234567890"
					"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
					"abcdefghijklmnopqrstuvwxyz"
					"-_"
				)
			# print(len(abc))
		self.update_abc(abc)

	@property
	def lenght_uuid(self):
	
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
		    num, digit = divmod(num, self.lenght_uuid) # len(self._abc)
		    result += self._abc[digit]
		
		return result

	def encode_s_uuid(self, _uuid):
		"""
		encodes a UUID into a string
		"""
		return self.num2str(_uuid.int >> 64)

	def encode_l_uuid(self, _uuid):
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

		return _id.uuid4()

	def _s_uuid(self):
		"""
		generate and return a UUID
		** uuid lenght is 11
		"""

		uuid = self._uu #_id.uuid4() #get_unique_txnid()

		return self.encode_s_uuid(uuid)

	def _l_uuid(self):
		"""
		generate and return a UUID
		** uuid lenght is 22
		"""

		uuid = self._uu

		return self.encode_l_uuid(uuid)


_inst = GenerateUUID()
suuid = _inst._s_uuid
luuid = _inst._l_uuid

"""
>>> import gen_uuid
>>> gen_uuid.luuid() # uuid lenght is 22
'mWPiqi5z_qQO-lr8L0LLu0'
>>> 
>>> import gen_uuid
>>> gen_uuid.suuid() # uuid lenght is 11
'KL3raivgvb5'
"""

# native uuid(universal unique identification) generation, callable from uuid module
# import uuid

def get_uuid_txnid():
	"""
	get universal unique identification
	>>> get_uuid_txnid()
	'10719362535681888741'
	"""
	return str(_id.uuid1().int >> 64)

def get_unique_txnid():
	"""
	get universal unique identification
	>>>  get_unique_txnid()
	'1009a807b4084628a2b727587103f110'
	"""
	return ''.join(str(_id.uuid4()).split('-'))