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
from __future__ import print_function

from meterplugin import PluginParameters
import sys
import os
import logging

logger = logging.getLogger(__name__)


class PluginRunner(object):
    def __init__(self, module_name, class_name):
        self.module_name = module_name
        self.class_name = class_name
        self.meter_plugin = None
        self.parameters = PluginParameters()
        self.collectors = []

    @staticmethod
    def usage():
        """
        Method to output the usage of plugin runner
        :return: None
        """
        sys.stderr.write("usage PluginRunner: <module name> <class name>\n")
        sys.exit(1)

    def load_plugin(self):
        sys.path.append(os.path.curdir)
        module = __import__(self.module_name)
        class_ = getattr(module, self.class_name)
        meter_plugin = class_()
        meter_plugin.initialize()
        self.meter_plugin = meter_plugin

    def create_collectors(self):
        """
        Generate the collectors from each of the parameter items
        :return: None
        """

        for item in self.parameters.get_items():
            collector = self.meter_plugin
            self.collectors.append(collector)

    def start_collectors(self):
        """
        Spawn a thread for each collector
        :return:
        """
        for collector in self.collectors:
            collector.start()

    def run(self):
        """
        1) Loads the class derived from Plugin
        2) Initializes and then runs Plugin
        :return: None
        """
        self.parameters.load()
        self.load_plugin()
        self.meter_plugin.parameters_loaded(self.parameters)
        self.meter_plugin.start()


def main():
    """
    Entry point for runnning plugins
    :return: None
    """
    print(sys.argv)
    if len(sys.argv) != 3:
        PluginRunner.usage()
    plugin_runner = PluginRunner(module_name=sys.argv[1], class_name=sys.argv[2])
    plugin_runner.run()


if __name__ == '__main__':
    main()
