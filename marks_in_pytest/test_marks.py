import pytest

@pytest.mark.first
def test_first_test():
    print("First test")

@pytest.mark.second
@pytest.mark.third
def test_second_test():
    print("Second test")