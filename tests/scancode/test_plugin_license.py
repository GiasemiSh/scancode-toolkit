#
# Copyright (c) 2018 nexB Inc. and others. All rights reserved.
# http://nexb.com and https://github.com/nexB/scancode-toolkit/
# The ScanCode software is licensed under the Apache License version 2.0.
# Data generated with ScanCode require an acknowledgment.
# ScanCode is a trademark of nexB Inc.
#
# You may not use this software except in compliance with the License.
# You may obtain a copy of the License at: http://apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
# When you publish or redistribute any data created with ScanCode or any ScanCode
# derivative work, you must accompany this data with the following acknowledgment:
#
#  Generated with ScanCode and provided on an "AS IS" BASIS, WITHOUT WARRANTIES
#  OR CONDITIONS OF ANY KIND, either express or implied. No content created from
#  ScanCode should be considered or used as legal advice. Consult an Attorney
#  for any legal advice.
#  ScanCode is a free software code scanning tool from nexB Inc. and others.
#  Visit https://github.com/nexB/scancode-toolkit/ for support and download.

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import os

import click
click.disable_unicode_literals_warning = True

from commoncode.testcase import FileDrivenTesting

from scancode.cli_test_utils import check_json_scan
from scancode.cli_test_utils import run_scan_click

test_env = FileDrivenTesting()
test_env.test_data_dir = os.path.join(os.path.dirname(__file__), 'data')

"""
Most of these tests spawn new process as if launched from the command line. Some
of these CLI tests are dependent on py.test monkeypatch to ensure we are testing
the actual command outputs as if using a real command line call. Some are using
a plain subprocess to the same effect.
"""

def test_license_option_reports_license_expressions():
    test_dir = test_env.get_test_loc('license-expression/scan', copy=True)
    result_file = test_env.get_temp_file('json')
    args = ['--license', '--strip-root', test_dir, '--json', result_file, '--verbose']
    run_scan_click(args)
    check_json_scan(test_env.get_test_loc('license-expression/scan.expected.json'), result_file, regen=False)
