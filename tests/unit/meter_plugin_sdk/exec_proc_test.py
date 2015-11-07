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

import unittest
from meter_plugin_sdk import ExecProc


class TestExecProc(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_constructor(self):
        e = ExecProc()
        self.assertTrue(e is not None, 'Instance is None')

    def test_missing_command(self):
        try:
            e = ExecProc()
            output = e.execute()
        except ValueError as v:
            self.assertEqual(type(v), ValueError)

    # def test_missing_path(self):
    #     try:
    #         e = ExecProc()
    #         e.command = ["-l"]
    #         output = e.execute()
    #     except ValueError as v:
    #         self.assertEqual(type(v), ValueError)

    def test_args_type(self):
        try:
            e = ExecProc()
            e.command = "-l"
        except ValueError as v:
            self.assertEqual(type(v), ValueError)

    # def test_exec(self):
    #     e = ExecProc()
    #     e.setCommand("ls -l src/test/resources/test-exec")
    #     output = e.execute()
    #     self.assertEquals(output,
    #                       "total 0\n"
    #                       "-rw-r--r--  1 davidg  staff  0 Aug 25 12:20 goodbye.txt\n"
    #                       "-rw-r--r--  1 davidg  staff  0 Aug 25 12:20 hello.txt\n"
    #                       "-rw-r--r--  1 davidg  staff  0 Aug 25 12:20 myDir\n")


if __name__ == '__main__':
    unittest.main()
