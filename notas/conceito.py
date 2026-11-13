def nota_para_conceito(nota):
    if nota < 0 or nota > 10:
        raise ValueError("nota deve estar entre 0 e 10")
    if nota >= 9.0:
        return "A"
    if nota >= 8.0:
        return "B"
    if nota >= 7.0:
        return "C"
    if nota >= 6.0:
        return "D"
    if nota >= 4.0:
        return "E"
    return "F"
