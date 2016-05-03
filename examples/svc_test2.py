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

class MyVariableSvc(object):
    pass

class AService(object):
    def __init__(self, param:MyVariableSvc):
        super(AService, self).__init__()
        print("MyService.__init__: %s" % param.__class__.__name__)

    def some_method(self, param:MyVariableSvc):
        print("MyService.some_method: %s" % param.__class__.__name__)

c = DI()
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

c.set(MyVariableSvc)
c.attempt(AService).set_signature().call("some_method", True)

print("Continer.get: %s" % c.get(AService).__class__.__name__)