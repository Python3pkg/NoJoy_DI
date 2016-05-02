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
# Timesamp: 5/1/16 :: 10:25 PM

class Service(object):

    _mytree = "one of my trees"
    _factory = None

    _classification = None
    _classification_getter = None
    _inject_arguments = False

    _locked = False

    def __init__(self, mycallable, classification):
        super(Service, self).__init__()

        self._kwargs = {}
        self._sets = {}
        self._calls = []
        self._configs = []
        self._arguments_configs = []
