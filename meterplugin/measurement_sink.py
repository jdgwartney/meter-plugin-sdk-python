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

from threading import Lock
from sys import stdout
import logging


logger = logging.getLogger(__name__)


class MeasurementSink(object):

    def send(self, metric=None, value=None, source=None, timestamp=None):
        pass


class MeasurementSinkStandardOut(MeasurementSink):

    lock = Lock()

    def __init__(self):
        pass

    def send(self, metric=None, value=None, source=None, timestamp=None):
        """
        Sends a measurement to standard out
        :param metric:
        :param value:
        :param source:
        :param timestamp:
        :return:
        """
        with MeasurementSinkStandardOut.lock:
            measurement = "{0} {1} {2} {3}".format(metric=metric, value=value, source=source, timestamp=timestamp)
            print(measurement)
            stdout.flush()


class MeasurementSinkAPI(MeasurementSink):

    def send(self, metric=None, value=None, source=None, timestamp=None):
        pass


class MeasurementSinkRPC(MeasurementSink):

    def send(self, metric=None, value=None, source=None, timestamp=None):
        pass

