#!/usr/bin/python
# -*- coding: utf-8 -*-
# NoJoy_DI (c) 2016 by Andre Karlsson<andre.karlsson@protractus.se>
#
# NorseBot is licensed under a
# Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License.
#
# You should have received a copy of the license along with this
# work.  If not, see <http://creativecommons.org/licenses/by-nc-nd/3.0/>
#
#
# Filename: svc_test.py by: andrek
# Timesamp: 2016-05-02 :: 14:19

import unittest
from container import Container

class MyParamService(object):
    pass

class MyService(object):
    def __init__(self, obj, text, value):
        super(MyService, self).__init__()
        print("service instance: %s" % obj)
        print("container parameter: %s" % text)
        print("provided value: %s" % value)

c = Container()

c.add_service(MyParamService)
c.add_variables('my-param', "value from container")
c.add_service(MyService).types(obj__svc=MyParamService, text__param="my-param", value="defined value")

c.get(MyService)