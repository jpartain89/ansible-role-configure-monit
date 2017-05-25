#!/usr/bin/env python

import os
import json

print json.dumps(os.listdir("/usr/local/etc/monit/conf.d/"))
