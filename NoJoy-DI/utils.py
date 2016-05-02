#!/usr/bin/python2.7
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
# Timesamp: 5/1/16 :: 10:23 PM

import functools
from inspect import isclass, isfunction

def object_name_standard(myobject):
    if isclass(myobject) or isfunction(myobject):
        return "{0}.{1}".format(myobject.__module__,myobject.__name__)
    if isinstance(myobject):
        return myobject

    print ("Error")

class LazyMarker(object):
    def __init__(self, service=None, function=None, variable=None):
        super(LazyMarker, self).init()
        self.service = service
        self.function = function
        self.variable = variable

    def transformer(self, getter, variable_getter):
        if self.service:
            s = getter(self.service)
            if self.function:
                return getattr(s, self.function)
            else:
                return s
        if self.variable:
            return variable_getter(self.variable)
        raise Exception()
