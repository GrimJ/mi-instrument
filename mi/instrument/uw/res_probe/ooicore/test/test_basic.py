#!/usr/bin/env python

__author__ = "Carlos Rueda"
__license__ = 'Apache 2.0'

"""
Unit tests for the basic trhph module.
"""


import mi.instrument.uw.res_probe.ooicore.trhph as trhph

from mi.core.unit_test import MiUnitTest
from nose.plugins.attrib import attr

@attr('UNIT', group='mi')
class BasicTrhphTest(MiUnitTest):
    """
    Unit tests for the basic trhph module.
    """

    def test_get_cycle_time(self):
        val = trhph.get_cycle_time(trhph.SYSTEM_PARAMETER_MENU)
        self.assertEqual(val, '20 Seconds')

    def test_get_verbose_vs_data_only(self):
        val = trhph.get_verbose_vs_data_only(trhph.SYSTEM_PARAMETER_MENU)
        self.assertEqual(val, 'Data Only')

    def test_get_power_statuses(self):
        res = trhph.get_power_statuses(trhph.SENSOR_POWER_CONTROL_MENU)
        self.assertEqual(res, ('On', 'On', 'On', 'On', 'On'))

    def test_get_system_info_metadata(self):
        (sn, so, ci, ss) = trhph.get_system_info_metadata(trhph.SYSTEM_INFO)
        self.assertEqual(sn, "Temperature Resistivity Probe - TRHPH")
        self.assertEqual(so, "Consortium for Ocean Leadership")
        self.assertEqual(ci, "Giora Proskurowski, 206-685-3507")
        self.assertEqual(ss, "001")
