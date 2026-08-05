def em_moeda(valor):
    if isinstance(valor, (int, float)):
        return f"R$ {valor:.2f}"
    return valor