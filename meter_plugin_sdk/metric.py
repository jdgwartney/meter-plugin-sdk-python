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


class Metric:
    def __init__(self,
                 name=None,
                 source=None,
                 timestamp=None,
                 value=None):
        # Define the member varibles
        self._source = None
        self._name = None
        self._timestamp = None
        self._value = None

        # set via properties
        self.name = name
        self.source = source
        self.timestamp = timestamp
        self.value = value

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, source):
        self._source = source

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        self._timestamp = timestamp

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __str__(self):

        return "{0} {1} {2}".format(self.name, self.value, self.source)

    def __repr__(self):
        return "{0}(name={1}, source={2}, timestamp={3}, value={4}".format('Metric',
                                                                           self.name,
                                                                           self.value,
                                                                           self.source,
                                                                           self.timestamp)
