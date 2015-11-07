# Copyright 2015 BMC Software, Inc.
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

import json
from pprint import pprint

try:
    import StringIO
except ImportError:
    from io import StringIO

from metric_item import MetricItem


class Configuration:
    def __init__(self, path):
        self.config = []
        self.path = path
        self.json_data = None
        self.data = None

    def set_path(self, path):
        self.path = path

    def get_entry_count(self):
        count = 0
        if self.data is not None:
            count = len(self.data['items'])
        return count

    def load(self):
        self.json_data = open(self.path)
        self.data = json.load(self.json_data)
        # Loop over the items and put into list
        metric_items = self.data['items']
        for i in metric_items:
            item = MetricItem()
            item.name = str(i['name'])
            item.polling_interval = int(i['pollInterval'])
            item.command = str(i['command'])
            item.debug = bool(i['debug'])
            self.config.append(item)

    def __str__(self):
        output = StringIO.StringIO()
        pprint(self.data, stream=output)
        return output.getvalue()

    def get_items(self):
        return self.config
