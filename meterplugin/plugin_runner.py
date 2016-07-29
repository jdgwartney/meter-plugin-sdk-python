#!/usr/bin/env python
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

from meterplugin import CollectorDispatcher
from meterplugin import MeasurementSinkStandardOut
from meterplugin import EventSinkStandardOut
import sys

# def my_excepthook(type, value, traceback):
#    sys.stderr.write("Unhandled error: {0}, {1}\n".format(type, value))

# sys.excepthook = my_excepthook


class PluginRunner(object):
    def __init__(self, module_name, class_name):
        self.module_name = module_name
        self.class_name = class_name
        self.dispatcher = CollectorDispatcher()

    @staticmethod
    def usage():
        sys.stderr.write("usage PluginRunner: <module name> <class name>\n")
        sys.exit(1)

    def run(self):
        module = __import__(self.module_name)
        class_ = getattr(module, self.class_name)
        meter_plugin = class_("")
        meter_plugin.initialize()
        meter_plugin.load_configuration()
        meter_plugin.set_measurement_output(MeasurementSinkStandardOut())
        meter_plugin.set_event_output(EventSinkStandardOut())


if __name__ == '__main__':
    if len(sys.argv) != 2:
        PluginRunner.usage()
    plugin_runner = PluginRunner()
    plugin_runner.run()
