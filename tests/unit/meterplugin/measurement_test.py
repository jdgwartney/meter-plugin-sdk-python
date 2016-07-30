# Copyright 2016 BMC Software, Inc.
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

from unittest import TestCase
from cStringIO import StringIO
import sys
from meterplugin import MeasurementSinkStandardOut
from tspapi import Measurement


class TestConfiguration(TestCase):

    def setUp(self):
        self.old_stdout = sys.stdout
        self.my_stdout = StringIO()
        sys.stdout = self.my_stdout

    def tearDown(self):
        sys.stdout = self.old_stdout

    def test_measurement_standard_out_sink(self):
        sink = MeasurementSinkStandardOut()
        m = Measurement(metric='FOO', value='100', source='BAR', timestamp=1500000000)
        sink.send(m)
        self.assertEqual('FOO 100 BAR 1500000000\n', self.my_stdout.getvalue())

