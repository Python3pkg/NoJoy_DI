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
#    Foobar is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
#
# Filename:  by: andrek
# Timesamp: 5/1/16 :: 10:25 PM

from utils import *
from trees import *
from functools import wraps
from importlib import import_module

#py3to2 hack
try:
	from inspect import signature, Parameter
	signature_empty = Parameter.empty
except ImportError:
	from funcsigs import signature
	from funcsigs import _empty as signature_empty

class Service(object):

	_mytree = SingletonTree
	_factory = None

	_classification = None
	_classification_getter = None
	_inject_signature = False

	_locked = False

	def __init__(self, mycallable, classification=None):
		super(Service, self).__init__()

		self._types = {}
		self._sets = {}
		self._callers = []
		self._injectors = []
		self._arguments_injectors = []

		self.name = object_name_standard(mycallable)

		if classification:
			self._classification = classification
		else:
			if callable(mycallable):
				self._classification = mycallable
			else:
				self._classification_getter = self._lazy_loader(mycallable)


	def _get_classification(self):
		if self._classification:
			return  self._classification
		if self._classification_getter:
			self._classification = self._classification_getter()
			return self._classification

		raise Exception()

	def _lazy_loader(self, class_hierarchy):
		module, cls = class_hierarchy.split('.', 1)
		@wraps(self._lazy_loader)
		def wrapper(*args, **kwargs):
			return getattr(import_module(module), cls)
		return  wrapper


	def _lazymarker(self, myclone=None, myservice=None, myfunction=None, myvariable=None):
		if not myclone is None:
			return myclone
		elif myservice or myvariable:
			return LazyMarker(service=myservice, function=myfunction, variable=myvariable)

	def _type_maker(self, kwargs):
		types = {}
		for key, value in kwargs.items():
			if key.endswith("__svc"):
				types[key[:-5]] = self._lazymarker(myservice=value)
			elif key.endswith("__param"):
				types[key[-7]] = self._lazymarker(myvariable=value)
			else:
				types[key] = value
		return types

	@lock_wrapper
	def set_classification(self, value):
		self._classification = value

	@lock_wrapper
	def set_factory(self, service=None, function=None, clone=callable):
		self._factory = self._lazymarker(myclone=clone, myservice=service, myfunction=function)

	@lock_wrapper
	def types(self, **kwargs):
		self._types.update(self._type_maker(kwargs))
		print(self._types)

	@lock_wrapper
	def call(self, function, **kwargs):
		self._callers.append((False, function, self._type_maker(kwargs)))

	@lock_wrapper
	def call_with_signature(self, function, **kwargs):
		self._callers.append((True, function, self._type_maker(kwargs)))

	@lock_wrapper
	def set(self, **kwargs):
		self._sets.update(self._type_maker(kwargs))

	@lock_wrapper
	def injector(self, service=None, function=None, function_args=None,
	             callable=None, callable_args=None):
		if function or callable:
			self._injectors.append(self._lazymarker(clone=callable, myservice=service, myfunction=function))
		if function_args or callable_args:
			self._arguments_injectors.append(self._lazymarker(
				myclone=callable, myservice=service,
				myfunction=function_args))

	@lock_wrapper
	def set_signature(self):
		self._inject_signature = True

	@lock_wrapper
	def tree(self, tree_cls):
		self._mytree = tree_cls
