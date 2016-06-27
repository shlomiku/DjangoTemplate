from .common import *  # noqa
from .local import SECRET_KEY

INSTALLED_APPS += ('django_nose',)
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
   '--with-coverage',  # activate coverage report
    '--with-doctest',  # activate doctest: find and run docstests
    '--verbosity=2',   # verbose output
    '--with-xunit',    # enable XUnit plugin
    '--xunit-file=shippable/testresults/nosetests.xml',  # the XUnit report file
    '--cover-xml',     # produle XML coverage info
    '--cover-xml-file=coverage.xml',  # the coverage info file
    # You may also specify the packages to be covered here
    # '--cover-package=blog,examples'
]
########## CELERY
# In development, all tasks will be executed locally by blocking until the task returns
CELERY_ALWAYS_EAGER = True
########## END CELERY



