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

from threading import Thread
import time
from meter_plugin_sdk import ExecProc
from sys import stdout


class MetricThread(Thread):
    def __init__(self, item, mutex):
        Thread.__init__(self, name=item.name)
        self.setDaemon(True)
        self.mutex = mutex
        self.pollingInterval = item.getPollingInterval()
        self.name = item.name
        self.proc = ExecProc()
        self.proc.command = item.command
        self.proc.debug = item.getDebug

    def run(self):  # run provides thread logic
        while True:
            output = self.proc.execute()
            with self.mutex:
                stdout.write(output.decode('utf-8'))
                stdout.flush()
            time.sleep(self.pollingInterval)
