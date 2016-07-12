# this is an attempt to deal with an issue on circle ci that keeps on coming back.
# some of the builds fail due to postgres container errors - listening to port 5432.
# when this happens - this trick solves that.
# whe it doesn't - this causes an error and fails the tests.
# wrapping it with try-except block should make this work continuously

import os

try:
    print os.popen("docker exec `docker ps |grep postgres|awk '{print $1}'` apt-get update").read()
    print os.popen("docker exec `docker ps |grep postgres|awk '{print $1}'` apt-get install -y net-tools").read()
except Exception:
    pass # do nothing. everything works.
