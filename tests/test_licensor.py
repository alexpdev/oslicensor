"""
Unit tests for the OSLicensor program.
"""
import sys
import os
import shutil

import pytest

from oslicensor import execute
from oslicensor.commands import LICENSES, get_command


@pytest.fixture(scope="module")
def testdir():
    """Test unittests in a temporary directory."""
    current = os.getcwd()
    parent = os.path.dirname(__file__)
    tempdir = os.path.join(parent, "tempdir")
    os.mkdir(tempdir)
    os.chdir(tempdir)
    yield tempdir
    os.chdir(current)
    shutil.rmtree(tempdir)


@pytest.mark.parametrize("code", list(LICENSES.keys()))
def test_command_get(code, testdir):
    """Test the get command."""
    _ = testdir
    cwd = os.getcwd()
    lic = os.path.join(cwd, "LICENSE")
    get_command(code)
    assert os.path.exists(lic)


@pytest.mark.parametrize("code", list(LICENSES.keys()))
def test_cli_get(code, testdir):
    """Test the get command through the cli."""
    _ = testdir
    sys.argv = ['oslicensor', 'get', code]
    cwd = os.getcwd()
    lic = os.path.join(cwd, "LICENSE")
    execute()
    assert os.path.exists(lic)
