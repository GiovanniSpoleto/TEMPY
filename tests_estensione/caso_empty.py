import pytest

def test_vuoto_pass():
    pass

def test_vuoto_ellipsis():
    ...

def test_vuoto_doc_commento():
    """ancora da scrivere"""
    # TODO
    pass

def test_pass_commento_inline():
    pass  # todo

def test_con_assert():
    assert 1 + 1 == 2

def test_codice_senza_assert():
    x = 1

def test_con_raises():
    with pytest.raises(ValueError):
        int("a")

def helper_vuoto():
    pass

class TestClasse:
    def test_metodo_vuoto(self):
        pass

    def test_metodo_pieno(self):
        assert True
