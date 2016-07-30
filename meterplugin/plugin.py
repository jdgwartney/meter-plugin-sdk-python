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


from meterplugin import PluginParameters
import logging
import sys

logger = logging.getLogger(__name__)


class Plugin:
    
    def __init__(self, path):
        self.parameters = PluginParameters(path)

    def _initialize(self):
        self.parameters.load()

    def plugin_initialize(self):
        pass

    def start(self):
        pass

    def create_collector(self, parameters):
        pass

    def run(self):
        self.dispatcher.run()

