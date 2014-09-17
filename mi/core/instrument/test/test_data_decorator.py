#!/usr/bin/env python

"""
@package ion.services.mi.test.test_data_decorator
@file ion/services/mi/test/test_data_decorator.py
@author Steve Foley
@brief Some unit tests for R2 instrument agent data decorators
"""

__author__ = 'Steve Foley'
__license__ = 'Apache 2.0'

import logging
import unittest
from mi.core.unit_test import MiUnitTest
import re
from nose.plugins.attrib import attr
from mock import Mock
from mi.core.instrument.data_decorator import RSNTimestampDecorator

import mi.core.mi_logger
mi_logger = logging.getLogger('mi_logger')

#@unittest.skip('Do not run hardware test.')
@attr('UNIT', group='mi')
class TestRSNDataDecorator(MiUnitTest):

    def setUp(self):
        self.decorator = RSNTimestampDecorator()
    
    @unittest.skip('not finished yet')
    def test_timestamp_split(self):
        good_timestamp = "<OOI-TS 2012-04-11T23:39:53.092182 TS>\r\nh<\00I-TS>"
        good_multiline_timestamp = "<OOI-TS 2012-04-11T23:39:56.620364 TS>\r\n\r\nInvalid command\r\n\r\n$<\00I-TS>"
        bad_timestamp = "<OOI-TS 2012-04-11T23:39:53.092182 TS>\r\nh<\FOO-TS>"
            
        self.assertEquals((None, None),
                          self.decorator.handle_incoming_data(bad_timestamp))
        
        self.assertEquals(("2012-04-11T23:39:53.092182", "\r\nh"),
                          self.decorator.handle_incoming_data(good_timestamp))
        
        self.assertEquals(("2012-04-11T23:39:56.620364", "\r\n\r\nInvalid command\r\n\r\n$"),
                          self.decorator.handle_incoming_data(good_timestamp))
