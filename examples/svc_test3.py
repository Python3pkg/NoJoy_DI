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

from NoJoy_DI.di import DI
from NoJoy_DI.patterns import BorgPattern, SingletonPattern, DefaultPattern


class MyVariableSvc(object):
	pass



class AClass(object):
	def __init__(self):
		self.b = "as"

class AnotherClass(object):
	def __init__(self, dep):
		super(AnotherClass, self).__init__()
		self.dep = dep

di = DI()
di.attempt(AClass).set_pattern(SingletonPattern)
di.attempt(AnotherClass).input(dep__svc=AClass).set_pattern(DefaultPattern)


print(di.get(AnotherClass).__dict__)



