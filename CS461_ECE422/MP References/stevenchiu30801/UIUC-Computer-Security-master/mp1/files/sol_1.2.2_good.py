#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           *�Ek�/�!���2)��o[����,�-ƀ��������H�Q2�*���y1kH�d0XП�im_][��J���F�e�ۭ�+例����I���E�7ߖφ�nR��5����3:]��s=R"""
from hashlib import sha256
if sha256(blob).hexdigest() == "4fa328cffd1a038f2bb07cc33555afa9f57e78fdd4a6aa5e46cd7913786330d1":
	print "I come in peace."
else:
	print "Prepare to be destroyed!"
