#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
Desc: Simple Generate UUID (Universal Unique Identification)
"""

# python imports
import uuid as _id

__author__ = "Lasha Gogua"
__version__ = "0.1.0"


class GenerateUUID(object):
    """
    Desc: GenerateUUID class
    """
    def __init__(self, abc=None):
        if abc is None:
            abc = list(
                "1234567890"
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                "abcdefghijklmnopqrstuvwxyz"
                "-_"
            )

        self.__update_abc(abc)

    @property
    def __length_uuid(self):
        """
        Desc: length uuid
        """

        return int(len(self._abc))

    def num2str(self, num):
        """
        convert a number to a string, using the given combined data
        """

        result = ""
        while num:
            num, digit = divmod(num, self.__length_uuid)
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

    def __update_abc(self, abc):
        """
        Desc: update abc
        """

        get_combined_data = list(sorted(set(abc)))
        self._abc = get_combined_data

    @property
    def __uuid(self):
        """
        get universal unique identification
        """

        return _id.uuid1()

    def short_uuid(self):
        """
        generate and return a UUID
        ** uuid lenght is 11
        """

        uuid = self.__uuid #_id.uuid4() #get_unique_txnid()

        return self.encode_s_uuid(uuid)

    def long_uuid(self):
        """
        generate and return a UUID
        ** uuid lenght is 22
        """

        uuid = self.__uuid

        return self.encode_l_uuid(uuid)


instance = GenerateUUID()
suuid = instance.short_uuid
luuid = instance.long_uuid

"""
>>> import gen_uuid
>>> gen_uuid.luuid() # combined uuid lenght is 22
'mWPiqi5z_qQO-lr8L0LLu0'
>>>
>>> import gen_uuid
>>> gen_uuid.suuid() # combined uuid lenght is 11
'KL3raivgvb5'
"""
