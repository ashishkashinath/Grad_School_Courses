#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           4$��,�����K~5Պ��فӂo>�@"Mĥ�r��޳��oj��ҵ��S��]{[r�qR&ȖC�P��.eI�X������cA�&/�l���KP���'��F�7ؑoy;C�p��$[��6�L�E��="""
from hashlib import sha256
if(int(sha256(blob).hexdigest(), 16) % 2):
	print "I come in peace."
else:
	print "Prepare to be destroyed!"
