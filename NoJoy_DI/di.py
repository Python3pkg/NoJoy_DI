# -*- coding: utf-8 -*-
# NoJoy_DI (c) 2016 by Andre Karlsson<andre.karlsson@protractus.se>
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
#    along with NoJoy_DI.  If not, see <http://www.gnu.org/licenses/>.
#
# Filename:  by: andrek
# Timesamp: 5/1/16 :: 10:25 PM


import functools
import sys

from NoJoy_DI.service import Service
from NoJoy_DI.utils import *
from NoJoy_DI.patterns import *
#py3to2 hack
try:
    from inspect import signature, Parameter
    signature_empty = Parameter.empty
except ImportError:
    from funcsigs import signature
    from funcsigs import _empty as signature_empty


class DI(object):
	"""
	Joyiders Norse Dependency Injection Classifcation container!
	"""

	my_patterns = []
	my_patterns_cls = []

	def __init__(self):
		super(DI, self).__init__()
		self.services = {}
		self.variables = {}
		self.my_service_name = object_name_standard(self.__class__)
		#print(object_name_standard(self.__class__))
		self.create_patterns(SingletonPattern, DefaultPattern, BorgPattern)


	def create_patterns(self, *trees):
		these_patterns = []
		these_patterns_cls = []

		for tree in trees:
			if isinstance(tree, BasePattern):
				these_patterns.append(tree)
				these_patterns_cls.append(tree.__class__)
			else:
				these_patterns.append(tree())
				these_patterns_cls.append(tree)
		self.my_patterns = tuple(these_patterns)
		self.my_patterns_cls = dict([(obj, inst) for inst, obj in enumerate(tuple(these_patterns_cls))])

	def set(self, name):
		svc = Service(name)
		self.services[svc.name] = svc
		return svc


	def attempt(self, name,shared=False):
		if object_name_standard(name) not in self.services:
			s = Service(name)
			if isinstance(shared, bool) and shared:
				s.pattern=SingletonPattern
			self.services[s.name] = s
			return s
		return False

	def get(self, service):
		return self._get_data(service)

	def getRaw(self, service):
		return self.services[object_name_standard(service)]


	def add_variables(self, name, value):
		self.variables[name] = value


	def get_variables(self, name):
		if name in self.variables:
			return self.variables[name]
		else:
			raise Exception("Unknown variable name")


	def get_definition(self, myservice):
		"""
		Return The
		:param myservice:
		:return:
		"""
		name = object_name_standard(myservice)
		if not name in self.services:
			print("Raise Error unknown service")
		return self.services[name]


	def _get_data(self, myservice, req_tokens=None):
		name = object_name_standard(myservice)

		if name == self.my_service_name:
			return self

		if name not in self.services:
			print("Raise Error unknown service")

		service_definition = self.services.get(name)
		my_tree = service_definition._mypattern

		if not my_tree in self.my_patterns_cls:
			print("Raise Error unknown service")

		tree_idx = self.my_patterns_cls[my_tree]

		if not req_tokens:
			req_tokens = []
		else:
			req_tree = req_tokens[-1]._mypattern
			if req_tree and tree_idx > self.my_patterns_cls[req_tree]:
				print("Scope is too big")

		def transformer(v):
			if isinstance(v, LazyMarker):
				return v.transformer(lambda name: self._get_data(name, req_tokens + [service_definition]), self.get_variables)
			else:
				return v

		def service_maker():
			return self._make(service_definition, transformer)

		return self.my_patterns[tree_idx].get(service_maker, name)

	def _update_input_from_signature(self, function, types_kwargs):
		try:
			sig = signature(function)
		except ValueError:
			return

		for name, param in tuple(sig.parameters.items()):
			if name == "self":
				continue
			if param.annotation is signature_empty:
				continue
			object_name = object_name_standard(param.annotation)

			if object_name in self.services:
				types_kwargs.setdefault(name, LazyMarker(service=object_name))


	def _make(self, svc_def, transformer):
		svc_def._locked = True

		def transform_input(types_kwargs):
			return dict([(key, transformer(value)) for key, value in types_kwargs.items()])

		if svc_def._factory:
			cls = transformer(svc_def._factory)
		else:
			cls = svc_def._get_classification()

		types_kwargs = dict(svc_def._input)
		self._update_input_from_signature(cls.__init__, types_kwargs)

		types_kwargs = transform_input((types_kwargs))

		for config in svc_def._arguments_injectors:
			transformer(config)(types_kwargs)

		myinstance = cls(**types_kwargs)

		for config in svc_def._injectors:
			transformer(config)(myinstance)

		for key, value in transform_input(svc_def._sets).items():
			setattr(myinstance, key, value)

		for active_signature, caller_function, caller_input in svc_def._callers:
			callable = getattr(myinstance, caller_function)
			types_kwargs = dict(caller_input)
			if active_signature:
				self._update_input_from_signature(callable, types_kwargs)
			callable(**transform_input(types_kwargs))

		return myinstance
