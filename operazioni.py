def somma(a:float, b:float):
  if isinstance(a, (int, float)) and isinstance(b, (int, float)):
    return a + b

  else:
    return None

def sottrazione(a: float, b: float):
    # Verifichiamo che entrambi gli input siano numeri (int o float)
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b
    else:
        # Se uno dei due non è un numero, restituiamo None
        return None