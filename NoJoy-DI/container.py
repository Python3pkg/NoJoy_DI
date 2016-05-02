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
# Timesamp: 5/1/16 :: 10:25 PM


import functools

from service import Service
from utils import *


class Container(object):
	"""
	Joyiders Norse Dependency Injection Classifcation container!
	"""

	my_trees = []
	my_trees_cls = []

	def __init__(self):
		super(Container, self).__init__()
		self.services = {}
		self.variables = {}
		self.my_service_name = object_name_standard(self.__class__)
		print(object_name_standard(self.__class__))


	def set_base_tree(self, *basetree):
		my_trees = []
		my_trees_cls = []

		for tree in basetree:
			if isinstance(tree, NoJoyBase):
				my_trees.append(tree)
				my_trees_cls.append(tree.__class)
			else:
				my_trees.append(basetree())
				my_trees_cls.append(basetree)
		self.my_trees = tuple(my_trees)
		self.my_trees_cls = dict([(obj, inst) in enumerate(tuple(my_trees_cls))])


	def add_service(self, name):
		s = Service(name)
		self.services[s.name] = s
		return s


	def add_variables(self, name, value):
		self.variables[name] = value


	def get_variable(self, name):
		if name in self.variables:
			return self.variables[name]
		else:
			print("Unknown variable name")


	def get_definition(self, myservice):
		name = object_name_standard(myservice)
		if not name in self.services:
			print("Raise Error unknown service")
		return self.services[name]


	def get_data(self, myservice, req_tokens)
		name = object_name_standard(myservice)

		if name == self.my_service_name:
			return self

		if name not in self.services:
			print("Raise Error unknown servce")

		service_definition = self.services.get(name)

		my_tree = service_definition._mytree

		if not my_tree in self.my_trees_cls:
			print("Raise Error unknown servce")

		tree_idx = self.my_trees_cls[my_tree]

		if not req_tokens:
			req_tokens = []
		else:
			req_tree = req_tokens[-1]._mytree
			if req_tree and tree_idx > self.my_trees_cls[req_tree]:
				print("Scope are too big")

		def transformer(v):
			if isinstance(v, LazyMarker):
				return v.transformer(lambda name: self.get_data(name,
				                                                req_tokens + [service_definition]),
				                     self.get_variable)

				# Return the Service here some how, need to create it first so i know whgat to return


	def _make(self, svc_def, transformer):
		if svc_def._factory:
			cls = transformer(svc_def._factory)
		else:
			cls = svc_def.  ###get_service_settings###


	if __name__ == '__main__':
		c = Container()
