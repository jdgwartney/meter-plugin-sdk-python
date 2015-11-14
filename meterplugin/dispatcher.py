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

import random
import platform
from threading import Thread, Lock
from meterplugin import MetricThread


class Dispatcher(object):
    def __init__(self):
        self._config = None
        pass

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, config):
        self._config = config

    def print_metric(self, metric):
        print(metric + " " + str(random.randrange(0, 99)) + " " + platform.node())

    def print_output(self):
        self.print_metric("LOAD_1_MINUTE")
        self.print_metric("LOAD_5_MINUTE")
        self.print_metric("LOAD_15_MINUTE")

    def run(self):
        stdoutmutex = Lock()  # same as thread.allocate_lock()
        threads = []
        items = self.config.items()
        for i in items:
            #           print(i.getName())
            thread = MetricThread(item=i, mutex=stdoutmutex)  # make/ start 10 threads
            thread.start()  # starts run method in a thread
            threads.append(thread)
        for thread in threads:
            thread.join()  # wait for thread exits

    def execute(self, execute_process, inputs):
        pool = Pool(processes=len(inputs))
        print(type(execute_process))
        print(type(inputs))
        print(type(len(inputs)))
        results = pool.map(execute_process, inputs)
        pool.close()
        return all(results)
