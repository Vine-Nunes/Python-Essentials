def eh_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

def numero_de_dias(ano, mes):
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if mes < 1 or mes > 12 or ano < 1:
        return None  # Retorna None se os argumentos não fazem sentido

    # Verifica se fevereiro precisa de ser ajustado para anos bissextos
    if mes == 2:
        if eh_bissexto(ano):
            return 29
        else:
            return 28

    # Retorna o número de dias para os outros meses
    return dias_por_mes[mes]

# Teste da função com alguns casos
casos_de_teste = [
    (2020, 2, 29),  # Ano bissexto, fevereiro deve ter 29 dias
    (2021, 2, 28),  # Não bissexto, fevereiro deve ter 28 dias
    (2022, 4, 30),  # Abril sempre tem 30 dias
    (2023, 12, 31), # Dezembro sempre tem 31 dias
    (2000, 13, None),  # Mês inválido
    (0, 1, None),      # Ano inválido
]

for ano, mes, resultado_esperado in casos_de_teste:
    resultado_real = numero_de_dias(ano, mes)
    assert resultado_real == resultado_esperado, f"Erro para o ano {ano}, mês {mes}. Esperado: {resultado_esperado}, Obtido: {resultado_real}"

print("Todos os testes passaram!")
  