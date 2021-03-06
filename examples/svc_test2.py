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
# Filename:  by: andrek
# Timesamp: 5/2/16 :: 10:55 PM

from NoJoy_DI.di import DI
from NoJoy_DI.patterns import DefaultPattern, BorgPattern

class MyVariableSvc(object):
    var = "var"

class AService(object):
    def __init__(self, param:MyVariableSvc):
        super(AService, self).__init__()
        print(("MyService.__init__: %s" % param.__class__.__name__))

    def some_method(self, param:MyVariableSvc):
        print(("MyService.some_method: %s" % param.__class__.__name__))

di = DI()
mydict = {'className':'SomeClass',
          'properties':[
	          {'name':'response',
               'value':
                   {'type':'service','name':'response'}
               },
              {'name':'someFlag',
               'value':
                   {'type':'paramter','value':True}
               }
          ]}
#pp = pprint.PrettyPrinter(indent=2)
#pp.pprint(mydict)

di.set(MyVariableSvc)

myc1 = di.get(MyVariableSvc)
myc2 = di.get(MyVariableSvc)
myc2.var = "new_var"
#c.attempt(AService).set_signature().call("some_method", True)
print(myc1)
print(myc2)
print((myc1.var))
print((myc2.var))
myc3 = di.get(MyVariableSvc)
myc3.var = "another_var"
print(myc3)
print((myc1.var))
print((myc2.var))
print((myc3.var))
#print("Continer.get: %s" % c.get(AService).__class__.__name__)
