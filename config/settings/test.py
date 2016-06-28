from .common import *  # noqa
from .local import SECRET_KEY, CELERY_ALWAYS_EAGER, DEBUG

INSTALLED_APPS += ('django_nose',)
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '--with-coverage',  # activate coverage report
    '--cover-package=deliverance.users',
    '--with-doctest',  # activate doctest: find and run docstests
    '--verbosity=3',   # verbose output
    '--exe',   #
    '--with-xunit',    # enable XUnit plugin
    '--xunit-file=shippable/testresults/nosetests.xml',  # the XUnit report file
    '--cover-xml',     # produle XML coverage info
    '--cover-xml-file=shippable/codecoverage/coverage.xml',  # the coverage info file
    # You may also specify the packages to be covered here
    # '--cover-package=blog,examples'
]




