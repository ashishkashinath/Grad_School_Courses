#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           �ԬWr�����7j(&l�q0S]�*2�vK�=����� �?�#�$��B9BY�jd�<h��"��0Ϸ�]�
|�S/���'��R�x!��)� ߷_���[B�ǡVu
�sMd�V�b��b�ƷI%љ�{"""
from hashlib import sha256
h = sha256(blob).hexdigest()
if h == '13f9aa5e90fe036cab1f7436943032e9565b5c1b6cf214d2e596511b186d6b00' :
    print "I come in peace."
elif h == 'da865f49f9324b38310a8f76d632681811da418bc8826519e6142955a0fa0eeb' :
    print "Prepare to be destroyed!"

