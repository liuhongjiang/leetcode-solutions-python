#! /usr/bin/env python

# Run this file, it will run the test case for the latest modified python code file
# the test cases files are come from test_data directory


import argparse
import importlib
import inspect
import os
import sys
import glob
import json


class BColors(object):
    HEADER = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END_COLOR = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def color_print(string, color):
    print color + string + BColors.END_COLOR


def run_unittest(problem):
    print "Run test cases for ",
    color_print("[%s]" % problem, BColors.OK_BLUE)

    # load the solution
    module = importlib.import_module(problem)
    solution = getattr(module, 'Solution', None)

    # find the target method, there should be one and only one method, which
    # does not start with underscore('_')
    funcs = inspect.getmembers(solution(), inspect.ismethod)
    pub_funcs = filter(lambda x: not x[0].startswith('_'), funcs)
    func = pub_funcs[0][1]

    # load all the test data
    test_dir = _get_test_dir()
    test_datum = _load_data(test_dir + '/%s-testcases.data' % problem)
    for data in test_datum:
        result = func(*data["args"])
        if result != data["expect"]:
            color_print("args = [%s], expect = [%s], result = [%s]" % (data["args"], data["expect"], result),
                        BColors.FAIL)
            return

    color_print("pass unit test!", BColors.OK_GREEN)


def _get_test_dir():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.abspath(os.path.join(dir_path, 'test_data'))


def _load_data(filename):
    with open(filename) as fp:
        lines = map(lambda x: x.strip(), fp.readlines())
        lines = filter(lambda x: len(x), lines)
        lines = filter(lambda x: not x.startswith('#'), lines)
        return map(lambda x: json.loads(x), lines)


def get_modify_time(file_name):
    return os.stat(file_name).st_mtime


def _sorted_ls(pattern):
    return list(sorted(glob.glob(pattern), key=get_modify_time, reverse=True))


def _find_problem(issue_number):
    pattern = issue_number + '*.py' if issue_number else '*.py'
    problems = _sorted_ls(pattern)
    problems = filter(lambda name: not name.startswith('test'), problems)
    return problems[0]


def bootstrap():
    ap = argparse.ArgumentParser()
    ap.add_argument('issue_number', nargs='?', help="issue number")
    args = ap.parse_args(sys.argv[1:])
    problem = _find_problem(args.issue_number)
    run_unittest(problem[0:-3])


if __name__ == '__main__':
    bootstrap()
