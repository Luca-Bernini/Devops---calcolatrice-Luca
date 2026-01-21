import pytest
from operazioni import moltiplicazione


def test_moltiplicazione_positivi():
    """Test moltiplicazione di due numeri positivi"""
    assert moltiplicazione(3, 4) == 12
    assert moltiplicazione(5, 2) == 10
    assert moltiplicazione(1.5, 2) == 3.0


def test_moltiplicazione_negativi():
    """Test moltiplicazione con numeri negativi"""
    assert moltiplicazione(-3, 4) == -12
    assert moltiplicazione(-2, -5) == 10
    assert moltiplicazione(-1.5, 2) == -3.0


def test_moltiplicazione_zero():
    """Test moltiplicazione con zero"""
    assert moltiplicazione(0, 5) == 0
    assert moltiplicazione(5, 0) == 0
    assert moltiplicazione(0, 0) == 0


def test_moltiplicazione_decimali():
    """Test moltiplicazione di numeri decimali"""
    assert moltiplicazione(2.5, 4) == 10.0
    assert moltiplicazione(0.5, 0.5) == 0.25
    assert moltiplicazione(1.1, 2) == pytest.approx(2.2)


def test_moltiplicazione_input_invalidi():
    """Test moltiplicazione con input non validi"""
    assert moltiplicazione("3", 4) is None
    assert moltiplicazione(3, "4") is None
    assert moltiplicazione("a", "b") is None
    assert moltiplicazione(None, 5) is None
    assert moltiplicazione(5, None) is None
