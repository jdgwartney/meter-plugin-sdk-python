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


class MetricItem(object):

    def __init__(self):
        self._name = ""
        self._poll_interval = 5
        self._command = ""
        self._debug = False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if type(name) != str:
            raise ValueError
        self._name = name

    @property
    def poll_interval(self):
        return self._poll_interval

    @poll_interval.setter
    def poll_interval(self, poll_interval):
        if type(poll_interval) != int:
            raise ValueError
        self._poll_interval = poll_interval

    @property
    def debug(self):
        return self._debug

    @debug.setter
    def debug(self, debug):
        if type(debug) != bool:
            raise ValueError
        self._debug = debug

    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, command):
        if type(command) != str:
            raise ValueError
        self._command = command

