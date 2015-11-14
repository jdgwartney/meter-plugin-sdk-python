# Copyright BMC Software, Inc.
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
from meterplugin import Metric


class TestMetric(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_attributes(self):
        metric = Metric()
        metric.name = 'foo'
        metric.value = 10
        metric.source = 'localhost'
        self.assertEqual(metric.name, 'foo', 'Name does not match')
        self.assertEqual(metric.value, 10, 'Values does nto match')
        self.assertEqual(metric.source, 'localhost', 'Source does not match')

    def test_string(self):
        metric = Metric()
        metric.name = 'bar'
        metric.value = 100
        metric.source = 'snafu'
        self.assertEqual(str(metric), 'bar 100 snafu', 'String does not match')
