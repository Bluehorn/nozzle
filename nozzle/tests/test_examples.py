# -*- coding: utf-8 -*-

import pytest
import os
import sys
import subprocess


@pytest.mark.xfail(
        reason="not implemented, mapping from dagger to nozzle unclear")
def test_coffee_example(examples_dir):
    env = dict(os.environ)
    env["PYTHONPATH"] = os.pathsep.join(sys.path)
    subprocess.check_call([sys.executable, "-m", "coffee.app"],
                          cwd=examples_dir, env=env)

@pytest.fixture
def examples_dir():
    return os.path.join(os.path.dirname(__file__), "examples")
