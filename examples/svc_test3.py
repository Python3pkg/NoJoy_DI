#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
# NoJoy-DI (c) 2016 by Andre Karlsson<andre.karlsson@protractus.se>
#
# This file is part of NoJoy-DI.
#
#    NoJoy-DI is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Foobar is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
#
# Filename:  by: andrek
# Timesamp: 5/2/16 :: 11:36 PM

from NoJoy_DI.container import Container

class MyVariableSvc(object):
    pass

class AService(object):
    def __init__(self, param:MyVariableSvc):
        super(AService, self).__init__()
        print("MyService.__init__: %s" % param.__class__.__name__)

    def some_method(self,  param:MyVariableSvc, **kwargs):
        print("MyService.some_method: %s" % param.__class__.__name__)
        print("kwargs from container: ", kwargs.items())

c = Container()

c.add_service(MyVariableSvc)
c.add_service(AService).call("some_method", param=MyVariableSvc, ham="hamdata", spam="spamdata")

print("Continer.get: %s" % c.get(AService).__class__.__name__)