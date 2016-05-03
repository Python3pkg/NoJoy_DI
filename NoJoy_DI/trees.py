#!/usr/bin/python
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
#
# Filename: trees by: andrek
# Timesamp: 2016-05-02 :: 11:47

from random import randint

class BaseTree(object):

	def get(self, c, name):
		raise NotImplementedError()

class DefaultTree(BaseTree):

	def get(self, c, name):
		return c()

class SingletonTree(BaseTree):
	"""
	Lazy instantioation of the SInglton Pattern
	"""
	def __init__(self):
		super(SingletonTree, self).__init__()
		self.instances = {}

	def get(self, creator, name):
		if not name in self.instances:
			self.instances[name] = creator()
		return self.instances[name]

class RandomTree(BaseTree):
    """Returns new or cached instances based on random factor."""
    def __init__(self, randomity=3):
        super(RandomTree, self).__init__()
        self.rnd = randomity
        self.instances = {}

    def get(self, creator, name):
        if not name in self.instances or randint(0, self.rnd) == 0:
            self.instances[name] = creator()
        return self.instances[name]