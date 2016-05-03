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
from NoJoy_DI.container import Container
from NoJoy_DI.trees import DefaultTree, SingletonTree, BaseTree
import pprint

class MyParamService(object):
	pass

class MyService(object):
	def __init__(self, obj, text, value):
		super(MyService, self).__init__()
		print("service instance: %s" % obj)
		print("container parameter: %s" % text)
		print("provided value: %s" % value)
		print("I am: ", self.__class__)

c = Container()
mydict = {'className':'SomeClass',
          'properties':[
	          {'name':'response',
                         'value':
	                         {'type':'service','name':'response'}},
                        {'name':'someFlag',
                         'value':
	                         {'type':'paramter','value':True}
                         }
                        ]
          }
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(mydict)
c.attempt(MyParamService)
c.add_variables('Variable_name', "variable_data")
c.attempt(MyService, True).types(obj__svc=MyParamService, text__param="Variable_name", value="The DATA")

id = c.get(MyService)
id2 = c.getRaw(MyService)
print(id2.tree)