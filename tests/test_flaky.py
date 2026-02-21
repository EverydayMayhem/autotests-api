import pytest
import random

PLATFORM = 'Linux'

@pytest.mark.flaky(reruns=3, reruns_delay=4)
def test_flaky():
    assert random.choice([True, False])

@pytest.mark.flaky(reruns=3, reruns_delay=4, condition= PLATFORM == 'Windows')
def test_flaky_condition():
    assert random.choice([True, False])