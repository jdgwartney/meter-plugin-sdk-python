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

from meterplugin import MetricItem


class Configuration:

    def __init__(self, path):
        self.config = []
        self.path = path
        self.json_data = None
        self.data = None

    def set_path(self, path):
        """
        Sets the path to the configuration file param.json
        :param path:
        :return:
        """
        self.path = path

    def get_entry_count(self):
        """
        Returns the number of configuration items
        :return:
        """
        count = 0
        if self.data is not None:
            count = len(self.data['items'])
        return count

    def load(self):
        self.json_data = open(self.path)
        self.data = json.load(self.json_data)
        # Loop over the items and put into list
        config_items = self.data['items']
        for item in config_items:
            self.handle_config_item(self.config, item)

    def handle_config_item(self, config, item):
        """
        Derived classes need to override this method to handle their specific
        configuration items
        :param config:
        :param item:
        :return:
        """
        metric_item = MetricItem()
        metric_item.name = str(item['name'])
        metric_item.polling_interval = int(item['pollInterval'])
        metric_item.command = str(item['command'])
        metric_item.debug = bool(item['debug'])
        config.append(metric_item)

    def __str__(self):
        output = StringIO.StringIO()
        pprint(self.data, stream=output)
        return output.getvalue()

    def get_items(self):
        return self.config
