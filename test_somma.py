import pytest
from operazioni import somma # Importa la funzione somma dal file somma.py

def test_somma_numeri_interi():
    # Verifichiamo che la somma di 1 e 2 sia 3
    assert somma(1, 2) == 3

def test_somma_numeri_decimali():
    # Verifichiamo che la somma di 1.5 e 2.5 sia 4.0
    assert somma(1.5, 2.5) == 4.0

def test_somma_con_stringa_deve_essere_none():
    # Secondo la tua ultima implementazione di somma, con stringhe dovrebbe restituire None
    assert somma('a', 2) is None