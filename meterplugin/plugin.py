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


from meterplugin import Configuration
from meterplugin import Dispatcher
import logging
import sys

logging.basicConfig(stream=sys.stderr,
                    format='thread: %(threadName)s, file: %(filename)s, msg: %(message)s', level=logging.DEBUG)


class Plugin:
    
    def __init__(self, path):
        self.config = Configuration(path)
        self.dispatcher = Dispatcher()
        self.measurement_output = None
        self.event_output = None

    def load_configuration(self):
        pass

    def set_measurement_output(self, output):
        self.measurement_output = output

    def set_event_output(self, output):
        self.event_output = output
        
    def initialize(self):
        self.config.load()
        self.dispatcher.config = self.config
    
    def run(self):
        self.dispatcher.run()

