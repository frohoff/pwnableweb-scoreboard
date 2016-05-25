# Copyright 2014 David Tomaschik <david@systemoverlord.com>
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

import sys
from time import sleep

from scoreboard.app import app
from scoreboard import models
from scoreboard import rest
from scoreboard import views

# Imported just for views
modules_for_views = (rest, views)

if __name__ == '__main__':
    if 'checkdb' in sys.argv:
        print("checking for db")
        models.db.engine.connect().close()
    elif 'waitdb' in sys.argv:
        print("waiting for db")
        timeout = int(sys.argv[2] or "5")
        while True:
          try:
            print("checking for db")
            models.db.engine.connect().close()
            break
          except Exception: 
            if timeout <= 0:
              raise
            else:
              time.sleep(1)
    elif 'createdb' in sys.argv:
        print("creating db")
        models.db.create_all()
    elif 'createdata' in sys.argv:
        print("creating db and data")
        from scoreboard.tests import data
        models.db.create_all()
        data.create_all()
    else:
        app.run(host='0.0.0.0', debug=True, port=app.config.get('PORT', 9999))
