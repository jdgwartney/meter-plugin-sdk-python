#!/usr/bin/env python
# Copyright 2014 Boundary, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from meterplugin import MetricItem


class TestMetricItem(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        m = MetricItem();

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_constructor(self):
        m = MetricItem()

    def test_name(self):
        m = MetricItem();
        m.name = 'foo'
        self.assertEquals(m.name, 'foo', 'Names not equal')

    def test_name_type(self):
        m = MetricItem();
        m.name = 'foo'
        self.assertTrue(type(m.name) == str, 'Name is not a string')

    def test_poll_interval(self):
        m = MetricItem()
        m.poll_interval = 100
        self.assertEquals(m.poll_interval, 100, 'Poll intervals not equal')

    def test_poll_interval_type(self):
        m = MetricItem()
        m.poll_interval = 1000
        self.assertTrue(type(m.poll_interval) == int)

    def test_poll_interval_debug(self):
        m = MetricItem()
        m.debug = True
        self.assertEquals(m.debug, True, 'Debug not equal')

    def test_command(self):
        m = MetricItem()
        m.command = 'snafu'
        self.assertEquals(m.command, 'snafu', 'Commands not equal')


if __name__ == '__main__':
    unittest.main()
