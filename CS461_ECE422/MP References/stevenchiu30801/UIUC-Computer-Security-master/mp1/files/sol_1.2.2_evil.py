#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           *�Ek�/�!���2)��o[�/��,�-ƀ��������H�Q2̋*���y1kH�d0XP��im_][��J���F�e�ۭ�+�5����I���E�7ߖφ�nR�x5����3:]���=R"""
from hashlib import sha256
if sha256(blob).hexdigest() == "4fa328cffd1a038f2bb07cc33555afa9f57e78fdd4a6aa5e46cd7913786330d1":
	print "I come in peace."
else:
	print "Prepare to be destroyed!"
