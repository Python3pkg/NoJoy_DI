#!/usr/bin/python
# -*- coding: utf-8 -*-
# NoJoy_DI (c) 2016 by Andre Karlsson<andre.karlsson@protractus.se>
#
# NorseBot is licensed under a
# Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License.
#
# You should have received a copy of the license along with this
# work.  If not, see <http://creativecommons.org/licenses/by-nc-nd/3.0/>
#
#
# Filename: svc_test.py by: andrek
# Timesamp: 2016-05-02 :: 14:19

import unittest
from NoJoy_DI.container import Container

class Test(unittest.TestCase):
	def testSignature(self):
		c = Container()

		class ParamClass(object): pass
		class MyClass(object):
			t = None
			m = None
			def __init__(self, t: ParamClass, a: str=None):
				super(MyClass, self).__init__()
				self.t = t

			def method(self, t: ParamClass):
				self.m = t

		c.add_service(ParamClass)
		c.add_service(MyClass).set_signature().call_with_signature("method")
		self.assertIsInstance(c.get(MyClass).t, ParamClass)
		self.assertIsInstance(c.get(MyClass).m, ParamClass)
