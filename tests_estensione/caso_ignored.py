import pytest
import unittest

@pytest.mark.skip
def test_skip():
    assert True

@pytest.mark.skip(reason="rotto")
def test_skip_con_motivo():
    assert True

@pytest.mark.skipif(1 > 2, reason="x")
def test_skipif():
    assert True

@pytest.mark.parametrize("n", [1, 2])
@pytest.mark.skip
def test_due_decorator(n):
    assert n

@pytest.mark.xfail
def test_xfail():
    assert True

@pytest.mark.parametrize("n", [1, 2])
def test_solo_parametrize(n):
    assert n

def test_normale():
    assert True

@pytest.mark.skip
def helper_skip():
    pass

class TestClasse:
    @unittest.skip("no")
    def test_unittest_skip(self):
        assert True

    @pytest.mark.skip
    def test_in_classe(self):
        assert True

    def test_ok(self):
        assert True

@pytest.mark.skipif(
    1 > 2,
    reason="multi riga")
def test_decorator_multiriga():
    assert True
