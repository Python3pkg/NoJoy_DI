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
#    NoJoy-DI is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with NoJoy-DI.  If not, see <http://www.gnu.org/licenses/>.
#
# Filename:  by: andrek
# Timesamp: 5/9/16 :: 8:02 PM

from NoJoy_DI.di import DI
from NoJoy_DI.service import Service
from NoJoy_DI.patterns import DefaultPattern, SingletonPattern, BasePattern


class TestPython2:
	def test_injector(self):
		di = DI()

		class AnInjector_Class(object):
			def injector(self, arg):
				arg.injected = True

			def injector_input(self, input):
				input["arg"] = "Injected argument arg"

		class AClass(object):
			injected = False

			def __init__(self, arg):
				super(AClass, self).__init__()
				self.arg = arg

			def injected_status(self):
				return self.injected

		di.attempt(AnInjector_Class)
		di.attempt(AClass).injector(service=AnInjector_Class, function="injector", function_args="injector_input")

		obj = di.get(AClass)
		assert obj.arg == "Injected argument arg"
		assert obj.injected_status

	def test_variables(self):
		class AClass(object):
			variable = "var Value"

		di = DI()

		di.add_variables("variable", "new var value")
		di.attempt(AClass).set(variable__param="variable").set(additional_variable="another value")
		obj = di.get(AClass)
		print(obj.additional_variable)

		assert obj.variable == "new var value"
		assert obj.additional_variable == "another value"

	def test_patternizer(self):
		class AClass(object):
			pass
		class AnotherClass(object):
			def __init__(self, dep):
				super(AnotherClass, self).__init__()
				self.dep = dep

		di = DI()
		di.attempt(AClass).pattern = DefaultPattern
		di.attempt(AnotherClass).set_pattern(SingletonPattern).input(dep__svc=AClass)

		#TODO: Check for exceptions instead of valid instance
		assert isinstance(di.get(AnotherClass).dep, AClass)
		assert di.get(AnotherClass) == di.get(AnotherClass)

	def test_factory(self):
		class AFactory(object):
			def manufacture(self, *args, **kwargs):
				return AClass(*args, **kwargs)

		class AClass(object):
			def __init__(self, an_argument):
				super(AClass, self).__init__()
				self.an_argument = an_argument

		di = DI()
		di.attempt(AFactory)
		di.attempt(AClass).set_factory(service=AFactory, function="manufacture").input(an_argument="The Argument")

		obj = di.get(AClass)

		assert isinstance(obj, AClass)
		assert obj.an_argument == "The Argument"

	def test_constructor(self):
		class AClass(object):
			def __init__(self, constructor_argument):
				super(AClass, self).__init__()
				self.constructor_argument = constructor_argument

		di = DI()
		di.attempt(AClass).input(constructor_argument="A Constructor variable value")

		assert di.get(AClass).constructor_argument == "A Constructor variable value"


