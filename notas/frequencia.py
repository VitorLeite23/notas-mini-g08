def frequencia_ok(presencas, aulas):
    if aulas <= 0:
        raise ValueError("aulas deve ser maior que 0")
    return 4 * presencas >= 3 * aulas
