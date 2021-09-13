# -*- encoding: utf-8 -*-

# per convention testing should always be isolated from main environment
# the testing environment is also named with a single leading underscore, thus
# defining it as an internal sub-module for `pkg-name` and thus not to be
# imported by default.
# the module can also be used by `.travis.yml` to run specific tests and
# generate build reports as per requirements.

# all the tests can also be listed in a file `run_tests.py`
# and is called by Travis CI for checking.
# update/change `.travis.yml` as per requirement.
