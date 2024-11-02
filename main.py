def calcPaga(horas, costeHora):
    """
    Calcula la paga total considerando horas extras a una tarifa de 1.5 veces el costo por hora.
    
    >>> calcPaga(35, 10)
    350.0
    >>> calcPaga(45, 10)
    475.0
    >>> calcPaga(40, 15)
    600.0
    """
    if horas <= 40:
        paga_total = float(horas * costeHora)
    else:
        horas_extras = horas - 40
        paga_total = float((40 * costeHora) + (horas_extras * costeHora * 1.5))
    return paga_total

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    # Interacción con el usuario
    try:
        horas = float(input("Introduce el número de horas trabajadas: "))
        costeHora = float(input("Introduce el coste por hora: "))
        paga = calcPaga(horas, costeHora)
        print(f"La paga total es: {paga}")
    except ValueError:
        print("Por favor, introduce valores numéricos válidos.")
