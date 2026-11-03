import pytest

def test_assert_true():
    assert True

def test_assert_uno():
    assert 1

def test_stesso_valore(x):
    assert x == x

def test_letterali():
    assert 2 == 2

def test_due_righe_su_tre():
    y = 3
    assert y == y
    assert y == 3
    assert True

def test_normale():
    assert 1 + 1 == 2

def test_diverso():
    a, b = 1, 2
    assert a != b

def test_con_messaggio():
    x = 1
    assert x == x, "sempre vero"

def test_commento_inline():
    assert True  # banale

def helper(x):
    assert x == x

class TestClasse:
    def test_in_classe(self):
        v = 2
        assert v == v

    def test_in_classe_ok(self):
        assert self.__class__ is not None
