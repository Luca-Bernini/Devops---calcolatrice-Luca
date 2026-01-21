# README

Questo codice contiene una semplice calcolatrice che esegue l'operazione di:
- somma tra due numeri

Include anche test unitari per verificare il corretto finzionamento della funzione somma

- verifica che l'interprete sia quello giusto
    - where python3 (Windows)

- Installare le dipendenze
    - pip install pytest

## Esecuzione normale
python calcolatrice.py

## Esecuzione dei test
pytest test_calcolatrice.py

## Installazione ambiente virtuale
    - py -m venv .venv

## rimozione old venv
    - rd /s /q .venv

## creazione venv con uv
    - uv venv
    -.venv\Scripts\activate

## per mettere in un requirements.txt in da un requirements.in che mette tutte le versioni

    uv pip compile requirements.in -o requirements.txt

## installazione dei requirements
    uv pip install -r requirements.txt  

## GitHub
    - git init

## collegamento alla repo con link http dopo origin
    - git remote add origin

## commit al main branch 
    - git add
    - git commit -m "commento"
    - git branch -M main
    - git push -u origin main
