import pytest
# Assumiamo che creerai un file chiamato sottrazione.py con la funzione sottrazione
from operazioni import sottrazione

def test_sottrazione_numeri_interi():
    # Caso base: 10 - 5 = 5
    assert sottrazione(10, 5) == 5

def test_sottrazione_risultato_negativo():
    # Verifichiamo che gestisca i risultati negativi: 3 - 10 = -7
    assert sottrazione(3, 10) == -7

def test_sottrazione_decimali():
    # Verifichiamo i numeri con la virgola: 5.5 - 2.5 = 3.0
    assert sottrazione(5.5, 2.5) == 3.0

def test_sottrazione_con_input_non_valido():
    # Se passiamo una stringa, la funzione dovrebbe restituire None (come per la somma)
    assert sottrazione('10', 5) is None