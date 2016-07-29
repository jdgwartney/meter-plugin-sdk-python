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
import os
from meterplugin import PluginParameters


class TestConfiguration(unittest.TestCase):

    def setUp(self):
        super(TestConfiguration, self).setUp()
        self.filename = os.path.join(os.path.dirname(__file__), 'test_param.json')
        self.conf = PluginParameters(self.filename)

    def tearDown(self):
        super(TestConfiguration, self).tearDown()

    def test_constructor(self):
        conf = PluginParameters(self.filename)
        self.assertTrue(conf is not None)

    def test_entry_count(self):
        self.conf.load()
        self.assertEquals(self.conf.get_entry_count(), 4, "Entry count does not match")

    def test_items(self):
        self.conf.load()
        config = self.conf.get_items()
        self.assertEqual(len(config), 4)
        self.assertEquals(config[0].name, "Echo foo")
        self.assertEquals(config[0].poll_interval, 5)
        self.assertEquals(config[0].command, 'scripts/random.sh 0 99')
        self.assertEquals(config[1].name, "Echo bar")
        self.assertEquals(config[1].poll_interval, 5)
        self.assertEquals(config[1].command, 'scripts/random.sh 0 99')

    def test_empty_items(self):
        self.assertEquals(len(self.conf.get_items()), 0, "Items not equal to zero")


if __name__ == '__main__':
    unittest.main()
