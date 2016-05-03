#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# NoJoy-DI (c) 2016 by Andre Karlsson<andre.karlsson@protractus.se>
#
# This file is part of NoJoy_DI.
#
#    NoJoy_DI is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    NoJoy_DI is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
#
#
# Filename: svc_test.py by: andrek
# Timesamp: 2016-05-02 :: 14:19

import unittest
from NoJoy_DI.di import DI
from NoJoy_DI.service import Service
from NoJoy_DI.trees import DefaultTree, SingletonTree, BaseTree
import pprint

class VarClass(object):
	pass

class SuperSvc(object):
	def __init__(self, obj, text, value):
		super(SuperSvc, self).__init__()
		print("service instance: %s" % obj)
		print("container parameter: %s" % text)
		print("provided value: %s" % value)
		print("I am: ", self.__class__)


class AService(object):
	a = None
	b = None
	def __init__(self, param:VarClass):
		super(AService, self).__init__()
		self.a = param
		print("AService.__init__: %s" % param.__class__.__name__)

	def some_method(self, param:VarClass):
		self.b = param
		print("AService.some_method: %s" % param.__class__.__name__)

di = DI()
di.attempt(VarClass)
di.add_variables('Variable_name', "variable_data")
di.attempt(SuperSvc, True).types(obj__svc=VarClass, text__param="Variable_name", value="The DATA")

di.set(VarClass)
di.attempt(AService).set_signature().call("some_method", True)

print("Continer.get: %s" % di.get(AService).__class__.__name__)

id = di.get(SuperSvc)
id2 = di.getRaw(SuperSvc)

def test_answer():
	"""
	Simple test case to verify that the classes are instantiated as expected.
	:return:
	"""
	assert isinstance(id2, Service)
	assert isinstance(di.get(AService), AService)
	assert isinstance(id, SuperSvc)

